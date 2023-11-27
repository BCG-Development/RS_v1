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
search_logger = logging.getLogger("search_logger")
search_logger.setLevel(logging.DEBUG)

async def search_document_by_id(document_id):
    """
    Search for a document in the 'Stores' collection by ID.

    Args:
    - document_id: The ID of the document to search for.

    Returns:
    - dict: The document if found, None otherwise.

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

        # Convert the document_id to ObjectId
        document_id = int(document_id)

        # Search for the document by ID
        result = await collection.find_one({"_id": document_id})

        if result:
            search_logger.info(f"Document found with ID {document_id}")
            return result
        else:
            search_logger.warning(f"No document found with ID {document_id}")
            return None

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        search_logger.error(f"MongoDB error: {pe}")
        return None
    except Exception as e:
        # Log unexpected errors
        search_logger.error(f"Unexpected error: {e}")
        return None

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            search_logger.info("MongoDB client closed successfully.")