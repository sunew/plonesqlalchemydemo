from z3c.saconfig import GloballyScopedSession
from z3c.saconfig import EngineFactory

# Here you can get the parameters like username and password, database, etc.
# Will be processed on zope startup.

DEBUG = True

username = 'zitelab'
password = 'AwaymWad0'
host = '127.0.0.1'
port = '3306'
database = 'zitelabtest'
database2 = 'zitelabtest'

ZitelabDBEngine1 = EngineFactory(
    'mysql://%s:%s@%s:%s/%s' % (
        username,
        password,
        host,
        port,
        database),
    echo=DEBUG,
    convert_unicode=True,
    pool_recycle=3600)

ZitelabDBSession1 = GloballyScopedSession(engine='zitelab_test_engine_1')

# This one could be to a different database:
ZitelabDBEngine2 = EngineFactory(
    'mysql://%s:%s@%s:%s/%s' % (
        username,
        password,
        host,
        port,
        database2),
    echo=DEBUG,
    convert_unicode=True,
    pool_recycle=3600)

ZitelabDBSession2 = GloballyScopedSession(engine='zitelab_test_engine_2')
