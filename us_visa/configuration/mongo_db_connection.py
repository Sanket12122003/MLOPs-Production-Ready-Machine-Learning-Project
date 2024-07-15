import sys
from dotenv import load_dotenv
from us_visa.exception import USvisaException
from us_visa.logger import logging
import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()

load_dotenv()

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :   This class is responsible for connecting to MongoDB and providing access to the database.
    
    Output      :   Connection to MongoDB database
    On Failure  :   Raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise USvisaException(e, sys)

    def get_collection(self, collection_name):
        return self.database[collection_name]


# Test the MongoDB connection
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    try:
        mongo_client = MongoDBClient()
        # Test the connection by listing collections
        collections = mongo_client.database.list_collection_names()
        logging.info(f"Connected to MongoDB, collections: {collections}")
        print("Collections:", collections)
    except Exception as e:
        logging.error(f"Connection test failed: {e}")
        print(f"Connection test failed: {e}")
