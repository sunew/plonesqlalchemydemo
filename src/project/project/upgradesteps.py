# -*- coding: utf-8 -*-
from logging import getLogger
from zope import component

from z3c.saconfig.interfaces import IEngineFactory

from project.model.base import Base

log = getLogger('project:upgrades')


def runProfiles(site, profile_ids):
    """ """
    setup_tool = getattr(site, 'portal_setup')

    for profile_id in profile_ids:
        if hasattr(setup_tool, 'runAllImportStepsFromProfile'):
            if not profile_id.startswith('profile-'):
                profile_id = "profile-%s" % profile_id
            setup_tool.runAllImportStepsFromProfile(profile_id)
        else:
            setup_tool.setImportContext(profile_id)
            setup_tool.runAllImportSteps()
        log.info("Ran profile " + profile_id)


def runDefaultProfile(tool):
    """ Run default profile """
    site = tool.aq_parent
    runProfiles(site, ('project:default',))


def setupDb(tool):
    """ """
    site = tool.aq_parent
    factory = component.getUtility(IEngineFactory, name="projectengine")
    engine = factory()
    Base.metadata.create_all(engine)
    log.info("Setup project db tables")
