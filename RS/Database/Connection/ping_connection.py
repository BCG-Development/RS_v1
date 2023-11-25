import os
import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_CONNECTION_STRING")

connection_logger = logging.getLogger("connection_logger")
connection_logger.setLevel(logging.DEBUG)

async def connect_to_database():
    try:
        connection_logger.info("Connecting to MongoDB.....")
        client = AsyncIOMotorClient(uri)

        await client.server_info()

        databases = await client.list_database_names()
        for db_name in databases:
            connection_logger.info(f" - {db_name}")

        for db_name in databases:
            database = client[db_name]
            collections = await database.list_collection_names()
            connection_logger.info(f"\nCollections in '{db_name}':")
            for col_name in collections:
                connection_logger.info(f" - {col_name}")

    except Exception as e:
        connection_logger.error(f"Error connecting to MongoDB: {e}")
    finally:
        if client is not None:
            try:
                client.close()
                connection_logger.info("MongoDB client closed successfully.")
            except Exception as close_error:
                connection_logger.error(f"Error closing MongoDB client: {close_error}")
        else:
            connection_logger.warning("MongoDB client was not initialized.")

asyncio.run(connect_to_database())