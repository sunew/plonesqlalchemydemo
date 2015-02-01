# plonesqlalchemydemo
Demo of Zope/SQLAlchemy transaction integration 

The Zope and ZODB transaction machinery (with the handling of ConlictErrors etc.) gives the need for some extra care when using other databases. It is necessary to integrate the transactions.

Also, Zope is a multithreaded system, thread safe use of connections are needed.

See http://pypi.python.org/pypi/z3c.saconfig
and
http://pypi.python.org/pypi/zope.sqlalchemy/0.7.5

Note that everywhere they manually commit in these docs, it is NOT something you should do. This is because they use doctests, so the commits are for their own internal testing.

Also note when looking in the code of z3c.saconfig (well-documented in code) and zope.sqlalchemy, the work they go to to make sure we are thread safe.


## Examples

There are three examples in the code:

1) Using the ORM: the recommended way

2) Using reflection of an existing database: sometimes needed, especially in transition from an older system

3) defining your own session utility: Can be used bot with reflection and with ORM. Good for getting the database connection string (username, password, database name etc.) from somewhere else (global config).


## Getting started

1) Create the demo database in mysql by running 

    mysql_scripts/mysql_create_fresh_db.sh

A testuser and a schema is created.

2) run the buildout: installs a fresh plone and the needed modules. Look in profiles.cfg and versions.cfg

3) Start plone. Install the 'project' module via the plone control panel. This creates the demo table in the mysql demo database.

4) read the code, play with the three demo browser views.


