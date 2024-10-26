from pymongo.mongo_client import MongoClient
import pandas as pd
import json, os
from src.constants import *

#url
# uri = os.getenv("MONGO_DB_URL")

#create a new client and connectt to server
client = MongoClient(MONGO_DB_URL)

#create database name and collection name
# DATABASE_NAME=os.getenv("MONGO_DATABASE_NAME")
# COLLECTION_NAME=os.getenv("MONGO_COLLECTION_NAME")

df=pd.read_csv("notebooks/wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)