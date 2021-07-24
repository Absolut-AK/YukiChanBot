import pymongo
import discord
from pymongo import MongoClient
from MainDiscordCommand import accountCreation
client = MongoClient("mongodb+srv://Yuki:A2d0a0m4@yukibot.7pgwj.mongodb.net/YukiBotDB?retryWrites=true&w=majority")
db = client["YukiBotDB"]
collection = db["YukiBotDB"]

# post = {"id": 0, "name": "abuno"}

# collection.insert_one(post)
#find id
def ids(post_id):
    accountTF = db.collection.find_one({"_id": post_id})
    if accountTF == None:
        db.collection.insert_One({"_id": post_id})

def leaderBoardCollection():
    db.collection.find_many(sort=["coin", pymongo.DESCENDING, 5])

