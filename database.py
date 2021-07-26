import pymongo
import discord
import os
from profileStats import Stats
from pymongo import MongoClient
client = MongoClient('mongodb+srv://Yuki:A2d0a0m4@yukibot.7pgwj.mongodb.net/YukiBotDB?retryWrites=true&w=majority')
db = client["YukiBotDB"]
collection = db["YukiBotDB"]

# post = {"id": 0, "name": "abuno"}

# collection.insert_one(post)

#find id 
#Account Things ↓
def ids(post_id):
    accountTF = db.collection.find({"id": post_id})
    if accountTF == None:
        collection.insert_One({"id": post_id})
    else:
        return True

def leaderBoardCollection():
    db.collection.find_many(sort=["coin", pymongo.DESCENDING, 5])

def profile(id):
    stats = Stats(collection.find({"__id": id}))