"""API CONTROLLER"""

import pymongo 

def init_collection():
    """
    Initialize connection to the mongoDB database
    """
    # MONGO_URL only work for Windows environment, for linux replace the link by mongodb://172.17.0.1:27017/ 
    MONGO_URL = "mongodb://host.docker.internal:27017/"
    DB_NAME = "articledb"
    COLLECTION_NAME = "article"

    client = pymongo.MongoClient(MONGO_URL)
    database = client[DB_NAME]
    collection = database[COLLECTION_NAME]
    return collection