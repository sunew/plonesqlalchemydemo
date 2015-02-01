# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope import interface
from zope import schema

from sqlalchemy.sql import functions
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Sequence)

from project.model.base import Base


class ITestData(Interface):
    """
    """
    my_first_field = schema.Int(
                    title=u"First field",
                    required=True
                    )
    my_second_field = schema.TextLine(
                    title=u"Second field",
                    required=True
                    )
    my_third_field = schema.Text(
                    title=u"Third field",
                    required=True
                    )


class TestData(Base):
    interface.implements(ITestData)
    __tablename__ = "test_data"
    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}

    row_id = Column(Integer, Sequence(__tablename__ + "_row_id"),
                    primary_key=True)

    my_first_field = Column(Integer, nullable=False)
    my_second_field = Column(String(500), nullable=False)
    my_third_field = Column(String(2000))

    created = Column(DateTime, default=functions.now())
    edited = Column(DateTime, onupdate=functions.current_timestamp())
    edited_by = Column(String(50))
