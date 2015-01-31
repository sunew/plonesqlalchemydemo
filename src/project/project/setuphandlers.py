from logging import getLogger
from Products.GenericSetup.upgrade import _upgrade_registry
from zope import component
from z3c.saconfig.interfaces import IEngineFactory
from project.model.base import Base

log = getLogger('project:setuphandlers')

def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('project_various.txt') is None:
        return

    # Add additional setup code here
    portal = context.getSite()
    setupDb(portal)


def setupDb(site):
    """ """
    factory = component.getUtility(IEngineFactory, name="projectengine")
    engine = factory()
    Base.metadata.create_all(engine)
    log.info("Setup project db tables")


def isInstalled(site, product_name):
    qi = getattr(site, 'portal_quickinstaller')

    installed_ids = [p['id'] for p in qi.listInstalledProducts()]
    if product_name in installed_ids:
        return True
    return False


# adapted from Products/GenericSetup/tool/manage_doUpgrades
def runUpgradeSteps(site, profile_id, product_name, check_installed=True):
    """Perform all available upgrade steps for profile_id.
    """
    log.info("Running available upgrade steps for profile " + profile_id)

    if check_installed and not isInstalled(site, product_name):
        log.info("Product %s is not installed in site" % str(product_name))
        return

    setup_tool = getattr(site, 'portal_setup')
    # These have not been run:
    steps_to_run = setup_tool.listUpgrades(profile_id)

    step = None
    for step_info in steps_to_run:
        step = _upgrade_registry.getUpgradeStep(profile_id, step_info['id'])
        if step is not None:
            step.doStep(setup_tool)
            msg = "Ran upgrade step '%s' for profile %s. Source: %s, dest: %s" % (
                                                step.title,
                                                profile_id,
                                                str(step.source),
                                                str(step.dest))
            log.info(msg)

    # We update the profile version to the last one we have reached
    # with running an upgrade step.
    if step and step.dest is not None and step.checker is None:
        setup_tool.setLastVersionForProfile(profile_id, step.dest)

