# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.protect import CheckAuthenticator
from Products.statusmessages.interfaces import IStatusMessage

from sqlalchemy.ext.declarative import declarative_base
from z3c.saconfig import named_scoped_session

Base = declarative_base()
Session = named_scoped_session('projectsession')


def get_table(session, name):
    if Base.metadata.bind is None:
        Base.metadata.reflect(session.bind)
        Base.metadata.bind = session.bind

    return Base.metadata.tables[name]


class MyView(BrowserView):

    template = ViewPageTemplateFile('templates/usingmodel.pt')

    label = u'Using SQLAlchemy reflection'

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

        # we use sqlalchemy reflection to build the model for us,
        # for an existing database where we do not have a model
        # (or do not want to create a model).
        table = get_table(session, 'test_data')
        query = table.select()
        # How to select with a where clause:
        # query = table.select(whereclause=((table.c.my_first_field == myvalue)))
        query_result = session.execute(query)

        output = []
        for r in query_result:
            output.append('%s - %s - %s - %s' % (
                r.row_id,
                r.my_first_field,
                r.my_second_field,
                r.my_third_field)
            )

        return output

    def add_row(self):
        session = Session()
        table = get_table(session, 'test_data')
        data = {'my_first_field': 43,
                'my_second_field': 'qwertyæøå',
                'my_third_field': 'qwertyusdfgh fghrt fgthy'}
        myinsert = table.insert(values=data)
        result = session.execute(myinsert)

        if result.rowcount > 0:
            self.status.addStatusMessage(u"Added row.", type='info')
        else:
            self.status.addStatusMessage(u"Row not added, some error happened.", type='error')
