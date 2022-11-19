from tinydb import TinyDB, Query, where

database = TinyDB("database.json")
db_player = database.table("players")
db_tournament = database.table("tournament")
