from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase
import os

if not os.path.exists('db'):
    os.makedirs('db')

static_db = SqliteQueueDatabase('db/static.db')

class BaseModel(Model):
    class Meta:
        database = static_db

class SummonerSpells(BaseModel):
    id = TextField(unique=True, primary_key=True)
    name = TextField()
    description = TextField()
    tooltip = TextField()
    maxrank = IntegerField()
    cooldown = TextField()
    cooldownBurn = TextField()
    cost = TextField()
    costBurn = TextField()
    datavalues = TextField()
    effect = TextField()
    effectBurn = TextField()
    vars = TextField()
    key = TextField()
    summonerLevel = IntegerField()
    modes = TextField()
    costType = TextField()
    maxammo = TextField()
    range = TextField()
    rangeBurn = TextField()
    image = TextField()
    resource = TextField()

static_db.connect()
static_db.create_tables([SummonerSpells])
static_db.close()