from z3c.saconfig import GloballyScopedSession
from z3c.saconfig import EngineFactory

# Here you can get the parameters like username and password, database, etc.
# Will be processed on zope startup.

DEBUG = False

username = 'plonesqldemo'
password = 'AwaymWad0'
host = '127.0.0.1'
port = '3306'
database = 'plonesqldemo'
database2 = 'plonesqldemo'

DemoDBEngine1 = EngineFactory(
    'mysql://%s:%s@%s:%s/%s' % (
        username,
        password,
        host,
        port,
        database),
    echo=DEBUG,
    convert_unicode=True,
    pool_recycle=3600)

DemoDBSession1 = GloballyScopedSession(engine='demo_engine_1')

# This one could be to a different database:
DemoDBEngine2 = EngineFactory(
    'mysql://%s:%s@%s:%s/%s' % (
        username,
        password,
        host,
        port,
        database2),
    echo=DEBUG,
    convert_unicode=True,
    pool_recycle=3600)

DemoDBSession2 = GloballyScopedSession(engine='demo_engine_2')
