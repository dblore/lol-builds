from riotwatcher import LolWatcher, ApiError
import os
from dotenv import load_dotenv
from models.static_db import SummonerSpells

load_dotenv()

lol_watcher = LolWatcher(os.environ.get("API_KEY"))

def update_summoner_spells():
    region = "euw1"
    versions = lol_watcher.data_dragon.versions_for_region(region)
    summoner_spells_version = versions["v"]
    summoner_spells = lol_watcher.data_dragon.summoner_spells(summoner_spells_version)
    raw_data = summoner_spells["data"]
    spells = []
    
    for spell in raw_data:
        spells.append(
            {
                "id": spell,
                "name": raw_data[spell]["name"],
                "description": raw_data[spell]["description"],
                "tooltip": raw_data[spell]["tooltip"],
                "maxrank": raw_data[spell]["maxrank"],
                "cooldown": raw_data[spell]["cooldown"],
                "cooldownBurn": raw_data[spell]["cooldownBurn"],
                "cost": raw_data[spell]["cost"],
                "costBurn": raw_data[spell]["costBurn"],
                "datavalues": raw_data[spell]["datavalues"],
                "effect": raw_data[spell]["effect"],
                "effectBurn": raw_data[spell]["effectBurn"],
                "vars": raw_data[spell]["vars"],
                "key": raw_data[spell]["key"],
                "summonerLevel": raw_data[spell]["summonerLevel"],
                "modes": raw_data[spell]["modes"],
                "costType": raw_data[spell]["costType"],
                "maxammo": raw_data[spell]["maxammo"],
                "range": raw_data[spell]["range"],
                "rangeBurn": raw_data[spell]["rangeBurn"],
                "image": raw_data[spell]["image"],
                "resource": raw_data[spell]["resource"]
            }
        )

    SummonerSpells.insert_many(spells).execute()    

update_summoner_spells()