from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=64)),
    Column('last_name', String(length=64)),
    Column('company', String(length=64)),
    Column('username', String(length=64)),
    Column('domain_access', String(length=124)),
    Column('email', String(length=100)),
    Column('passwd', String(length=64)),
    Column('sudoer', String(length=64)),
    Column('shell', String(length=64)),
    Column('created', String(length=64)),
    Column('active', String, default=ColumnDefault('Active')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['shell'].create()
    post_meta.tables['user'].columns['sudoer'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['shell'].drop()
    post_meta.tables['user'].columns['sudoer'].drop()
