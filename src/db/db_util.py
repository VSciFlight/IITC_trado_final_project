import pymongo
from urllib.parse import quote

import pandas as pd

def create_connection_to_db():

    db_address = ''
    db_name = "trado_qa"

    client = pymongo.MongoClient(db_address)
    db = client[db_name]

    db_test_connection(db)

    return db


def db_test_connection(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)

