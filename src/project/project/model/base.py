# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from z3c.saconfig import named_scoped_session

Session = named_scoped_session("projectsession")

Base = declarative_base()
