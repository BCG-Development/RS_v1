import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the modify module
modify_logger = logging.getLogger("modify_logger")
modify_logger.setLevel(logging.DEBUG)

async def modify_document(document_id, store_restrictions):
    """
    Modify an existing document in the 'Stores' collection.

    Args:
    - document_id: The ID of the document to modify.
    - store_restrictions: The store restrictions to add or update.

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

        # Check if the document exists
        existing_document = await collection.find_one({"_id": int(document_id)})
        if not existing_document:
            modify_logger.warning(f"No document found with ID {document_id}. Cannot modify.")
            return

        # Update the store restrictions in the existing document
        await collection.update_one(
            {"_id": int(document_id)},
            {"$set": {"Store Restrictions": store_restrictions}}
        )

        modify_logger.info(f"Document with ID {document_id} modified successfully.")

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        modify_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        modify_logger.error(f"Unexpected error: {e}")

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            modify_logger.info("MongoDB client closed successfully.")
