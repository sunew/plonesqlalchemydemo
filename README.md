# plonesqlalchemydemo
Demo of Zope/SQLAlchemy transaction integration 

Three examples:

1) Using the ORM: the recommended way
2) Using reflection of an existing database: sometimes needed, especially in transition from an older system
3) defining your own session utility: Can be used bot with reflection and with ORM. Good for getting the database connection string (username, password, database name etc.) from somewhere else (global config).

See https://pypi.python.org/pypi/z3c.saconfig/0.13
and
https://pypi.python.org/pypi/zope.sqlalchemy/0.7.5#id1

Note that everywhere they manually commit in these docs, it is NOT something you should do. This is because they use doctests, so the commits are for their own internal testing.

