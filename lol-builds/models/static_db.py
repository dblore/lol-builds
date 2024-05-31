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
    cooldown = TextField()
    cooldownBurn = TextField()
    cost = TextField()
    costBurn = TextField()
    costType = TextField()
    datavalues = TextField()
    description = TextField()
    effect = TextField()
    effectBurn = TextField()
    image = TextField()
    key = TextField()
    maxammo = TextField()
    maxrank = IntegerField()
    modes = TextField()
    name = TextField()
    range = TextField()
    rangeBurn = TextField()
    resource = TextField()
    summonerLevel = IntegerField()
    tooltip = TextField()
    vars = TextField()

class Runes(BaseModel):
    id = TextField(unique=True, primary_key=True)
    key = TextField()
    icon = TextField()
    name = TextField()
    shortDesc = TextField()
    longDesc = TextField()

class RuneSlots(BaseModel):
    rune_1 = ForeignKeyField(Runes, primary_key=True)
    rune_2 = ForeignKeyField(Runes)
    rune_3 = ForeignKeyField(Runes)

class RuneKeys(BaseModel):
    id = TextField(unique=True, primary_key=True)
    key = TextField()
    icon = TextField()
    name = TextField()

static_db.connect()
static_db.create_tables([SummonerSpells, Runes, RuneSlots, RuneKeys])
static_db.close()
