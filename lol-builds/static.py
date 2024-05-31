from riotwatcher import LolWatcher, ApiError
import os
from dotenv import load_dotenv
from models.static_db import SummonerSpells, Runes, RuneSlots, RuneKeys, Items
import pprint

load_dotenv()

lol_watcher = LolWatcher(os.environ.get("API_KEY"))


def update_summoner_spells():
    region = "euw1"
    versions = lol_watcher.data_dragon.versions_for_region(region)
    summoner_spells_version = versions["v"]
    summoner_spells = lol_watcher.data_dragon.summoner_spells(summoner_spells_version)
    data = summoner_spells["data"]
    spells = []

    for spell in data:
        spells.append(
            {
                "id": spell,
                "cooldown": data[spell]["cooldown"],
                "cooldownBurn": data[spell]["cooldownBurn"],
                "cost": data[spell]["cost"],
                "costBurn": data[spell]["costBurn"],
                "costType": data[spell]["costType"],
                "datavalues": data[spell]["datavalues"],
                "description": data[spell]["description"],
                "effect": data[spell]["effect"],
                "effectBurn": data[spell]["effectBurn"],
                "image": data[spell]["image"],
                "key": data[spell]["key"],
                "maxammo": data[spell]["maxammo"],
                "maxrank": data[spell]["maxrank"],
                "modes": data[spell]["modes"],
                "name": data[spell]["name"],
                "range": data[spell]["range"],
                "rangeBurn": data[spell]["rangeBurn"],
                "resource": data[spell]["resource"],
                "summonerLevel": data[spell]["summonerLevel"],
                "tooltip": data[spell]["tooltip"],
                "vars": data[spell]["vars"],
            }
        )

    SummonerSpells.insert_many(spells).on_conflict_replace().execute()


def update_runes():
    region = "euw1"
    versions = lol_watcher.data_dragon.versions_for_region(region)
    runes_reforged_version = versions["v"]
    data = lol_watcher.data_dragon.runes_reforged(runes_reforged_version)
    runes = []
    keys = []
    slots = []

    for key in data:
        keys.append(
            {
                "id": key["id"],
                "key": key["key"],
                "icon": key["icon"],
                "name": key["name"],
            }
        )

        for slot in key["slots"]:
            slots.append(
                {
                    "rune_1": slot["runes"][0]["id"],
                    "rune_2": slot["runes"][1]["id"],
                    "rune_3": slot["runes"][2]["id"],
                }
            )

            for rune in slot["runes"]:
                runes.append(
                    {
                        "id": rune["id"],
                        "key": rune["key"],
                        "icon": rune["icon"],
                        "name": rune["name"],
                        "shortDesc": rune["shortDesc"],
                        "longDesc": rune["longDesc"],
                    }
                )

    Runes.insert_many(runes).on_conflict_replace().execute()
    RuneSlots.insert_many(slots).on_conflict_replace().execute()
    RuneKeys.insert_many(keys).on_conflict_replace().execute()


def update_items():
    region = "euw1"
    versions = lol_watcher.data_dragon.versions_for_region(region)
    item_version = versions["v"]
    item_list = lol_watcher.data_dragon.items(item_version)
    data = item_list["data"]
    items = []

    for item in data:
        try:
            into = data[item]["into"]
        except Exception:
            into = ""
        try:
            depth = data[item]["depth"]
        except Exception:
            depth = ""
        try:
            fromId = data[item]["from"]
        except Exception:
            fromId = ""
        try:
            inStore = data[item]["inStore"]
        except Exception:
            inStore = ""
        try:
            requiredAlly = data[item]["requiredAlly"]
        except Exception:
            requiredAlly = ""
        try:
            effect = data[item]["effect"]
        except Exception:
            effect = ""
        items.append(
            {
                "id": item,
                "name": data[item]["name"],
                "description": data[item]["description"],
                "colloq": data[item]["colloq"],
                "plaintext": data[item]["plaintext"],
                "into": into,
                "image": data[item]["image"],
                "gold": data[item]["gold"],
                "tags": data[item]["tags"],
                "maps": data[item]["maps"],
                "stats": data[item]["stats"],
                "depth": depth,
                "fromId": fromId,
                "inStore": inStore,
                "requiredAlly": requiredAlly,
                "effect": effect,
            }
        )

        Items.insert_many(items).on_conflict_replace().execute()


update_summoner_spells()
update_runes()
update_items()
