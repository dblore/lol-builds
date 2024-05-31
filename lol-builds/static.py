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
                "cooldown": raw_data[spell]["cooldown"],
                "cooldownBurn": raw_data[spell]["cooldownBurn"],
                "cost": raw_data[spell]["cost"],
                "costBurn": raw_data[spell]["costBurn"],
                "costType": raw_data[spell]["costType"],
                "datavalues": raw_data[spell]["datavalues"],
                "description": raw_data[spell]["description"],
                "effect": raw_data[spell]["effect"],
                "effectBurn": raw_data[spell]["effectBurn"],
                "image": raw_data[spell]["image"],
                "key": raw_data[spell]["key"],
                "maxammo": raw_data[spell]["maxammo"],
                "maxrank": raw_data[spell]["maxrank"],
                "modes": raw_data[spell]["modes"],
                "name": raw_data[spell]["name"],
                "range": raw_data[spell]["range"],
                "rangeBurn": raw_data[spell]["rangeBurn"],
                "resource": raw_data[spell]["resource"]
                "summonerLevel": raw_data[spell]["summonerLevel"],
                "tooltip": raw_data[spell]["tooltip"],
                "vars": raw_data[spell]["vars"],
            }
        )

    SummonerSpells.insert_many(spells).execute()    

update_summoner_spells()