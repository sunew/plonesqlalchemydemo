# -*- coding: utf-8 -*-
from z3c.saconfig import named_scoped_session

from project.browser.reflection_example import ReflectionView

# Here we use our own session utility defined in dbutility:
Session = named_scoped_session('demo_session_1')


class Reflection2View(ReflectionView):

    label = u'Using SQLAlchemy reflection and own session utility'
