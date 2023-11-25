# insert_many.py

import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging
import pandas as pd

load_dotenv()

uri = os.getenv("MONGO_CONNECTION_STRING")

insert_many_logger = logging.getLogger("insert_many_logger")
insert_many_logger.setLevel(logging.DEBUG)

async def insert_documents(file_path):
    try:
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            await _validate_and_insert(collection, row)

    except PyMongoError as pe:
        insert_many_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        insert_many_logger.error(f"Unexpected error: {e}")

    finally:
        if client:
            client.close()
            insert_many_logger.info("MongoDB client closed successfully.")

async def _validate_and_insert(collection, row):
    try:
        if 'Tail Lift' not in row:
            raise ValueError("Column 'Tail Lift' not found in the row.")

        tail_lift = bool(row["Tail Lift"])

        document = {
            "_id": row["ID"],
            "Store name": row["Store Name"],
            "Store Address": row["Store Address"],
            "Store Postcode": row["Store Postcode"],
            "Kilometers": row["Kilometers"],
            "Does the store require a tail lift? (True/False)": tail_lift
        }

        result = await collection.insert_one(document)
        insert_many_logger.info(f"Document inserted with ID: {result.inserted_id}")

    except ValueError as ve:
        insert_many_logger.error(f"Validation error: {ve}")
    except PyMongoError as pe:
        insert_many_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        insert_many_logger.error(f"Unexpected error: {e}")

