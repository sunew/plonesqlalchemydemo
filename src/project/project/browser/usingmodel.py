# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.protect import CheckAuthenticator
from Products.statusmessages.interfaces import IStatusMessage

from z3c.saconfig import named_scoped_session

from project.model.testdata import TestData

Session = named_scoped_session('projectsession')


class MyView(BrowserView):

    template = ViewPageTemplateFile('templates/usingmodel.pt')

    label = u'Using SQLAlchemy model'

    def __init__(self, context, request):
        super(MyView, self).__init__(context, request)

    def __call__(self):
        self.status = IStatusMessage(self.request)
        if self.request.form.has_key('submitted'):
            CheckAuthenticator(self.request)
            if self.request.form.has_key('add_row'):
                self.status.addStatusMessage(u"Added row.", type='info')
                self.add_row()

        return self.template()

    def rows(self):
        session = Session()
        # We use the model to query data:
        rows = session.query(TestData).all()

        # we could also just return the sqlalchemy objects to the view,
        # and let the view access the attributes as needed. But here it is
        # kept simple for demo purposes.
        output = []
        for r in rows:
            output.append('%s - %s - %s - %s' % (
                r.row_id,
                r.my_first_field,
                r.my_second_field,
                r.my_third_field)
            )

        return output

    def add_row(self):
        session = Session()
        data = {'my_first_field': 42,
                'my_second_field': 'qwertyæøå',
                'my_third_field': 'qwertyusdfgh fghrt fgthy'}
        new_row = TestData(**data)
        session.add(new_row)
