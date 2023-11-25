import os
import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the connection module
connection_logger = logging.getLogger("connection_logger")
connection_logger.setLevel(logging.DEBUG)

async def connect_to_database():
    """
    Connect to the MongoDB server, retrieve and log information about databases and collections.

    This coroutine establishes a connection to the MongoDB server using the specified URI.
    It then logs information about available databases and collections.

    Note: The asyncio.run() function is used to run this coroutine, assuming it is the entry point.

    Raises:
    - Exception: If an error occurs during the connection or database information retrieval process.
    """

    try:
        # Log connection attempt
        connection_logger.info("Connecting to MongoDB.....")

        # Establish a connection to the MongoDB server
        client = AsyncIOMotorClient(uri)

        # Check server info to verify the connection
        await client.server_info()

        # Retrieve and log information about available databases
        databases = await client.list_database_names()
        for db_name in databases:
            connection_logger.info(f" - {db_name}")

        # Retrieve and log information about collections in each database
        for db_name in databases:
            database = client[db_name]
            collections = await database.list_collection_names()
            connection_logger.info(f"\nCollections in '{db_name}':")
            for col_name in collections:
                connection_logger.info(f" - {col_name}")

    except Exception as e:
        # Log error if an exception occurs during the connection process
        connection_logger.error(f"Error connecting to MongoDB: {e}")

    finally:
        # Close the MongoDB client, log closure attempt, and handle potential errors
        if client is not None:
            try:
                client.close()
                connection_logger.info("MongoDB client closed successfully.")
            except Exception as close_error:
                connection_logger.error(f"Error closing MongoDB client: {close_error}")
        else:
            connection_logger.warning("MongoDB client was not initialized.")

# Run the connect_to_database coroutine using asyncio.run() as the entry point
asyncio.run(connect_to_database())
