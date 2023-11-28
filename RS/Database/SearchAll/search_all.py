import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the search module
search_all_logger = logging.getLogger("search_all_logger")
search_all_logger.setLevel(logging.DEBUG)

async def search_all():
    """
    Search for all documents in the 'Stores' collection.

    Returns:
    - list: A list of all documents in the 'Stores' collection.
            Each document is represented as a dictionary.

    Raises:
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
    client = None
    try:
        # Connect to the MongoDB database
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        # Search for all documents in the 'Stores' collection
        cursor = collection.find()
        result = await cursor.to_list(length=None)

        if result:
            search_all_logger.info(f"Found {len(result)} documents in the 'Stores' collection")
            return result
        else:
            search_all_logger.warning("No documents found in the 'Stores' collection")
            return None

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        search_all_logger.error(f"MongoDB error: {pe}")
        return None
    except Exception as e:
        # Log unexpected errors
        search_all_logger.error(f"Unexpected error: {e}")
        return None

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            search_all_logger.info("MongoDB client closed successfully.")
