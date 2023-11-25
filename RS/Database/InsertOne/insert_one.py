import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

load_dotenv()

uri = os.getenv("MONGO_CONNECTION_STRING")

insert_one_logger = logging.getLogger("insert_one_logger")
insert_one_logger.setLevel(logging.DEBUG)

def validate_tail_lift(tail_lift):
    try:
        if not isinstance(tail_lift, bool):
            raise ValueError("Invalid input for tail lift. Please enter True or False.")
    except ValueError as ve:
        insert_one_logger.error(f"Validation error: {ve}")
        return False
    return True

async def insert_document(id, store_name, store_address, store_postcode, kms, tail_lift):
    if not validate_tail_lift(tail_lift):
        return

    client = None
    try:
        # Connect to the MongoDB database
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        # Create a document to insert
        document = {
            "_id": int(id),
            "Store name": store_name,
            "Store Address": store_address,
            "Store Postcode": store_postcode,
            "Kilometers": kms,
            "Does the store require a tail lift? (True/False)": bool(tail_lift)
        }

        # Insert the document
        result = await collection.insert_one(document)
        insert_one_logger.info(f"Document inserted with ID: {result.inserted_id}")

    except PyMongoError as pe:
        insert_one_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        insert_one_logger.error(f"Unexpected error: {e}")

    finally:
        if client:
            client.close()
            insert_one_logger.info("MongoDB client closed successfully.")
