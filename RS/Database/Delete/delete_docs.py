import os
from bson import ObjectId
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the delete module
delete_logger = logging.getLogger("delete_logger")
delete_logger.setLevel(logging.DEBUG)

async def delete_one_document(document_id):
    """
    Delete a single document from the 'Stores' collection based on the provided document ID.

    Args:
    - document_id (str): The ID of the document to be deleted.

    Raises:
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
    try:
        # Log the start of the document deletion process
        delete_logger.info("Searching for document.....")

        # Establish a connection to the MongoDB server
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        # Convert the document_id to ObjectId if it's not already
        try:
            document_id = ObjectId(document_id)
        except Exception as e:
            pass

        # Construct the filter query based on the document_id type
        if isinstance(document_id, ObjectId):
            filter_query = {"_id": document_id}
        else:
            filter_query = {"_id": int(document_id)}

        # Perform the delete operation and log the result
        result = await collection.delete_one(filter_query)
        if result.deleted_count == 1:
            delete_logger.info(f"Document with ID {document_id} deleted successfully.")
        else:
            delete_logger.warning(f"No document found with ID {document_id}.")

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        delete_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        delete_logger.error(f"Unexpected error: {e}")

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            delete_logger.info("MongoDB client closed successfully.")

async def delete_many_documents(criteria='all'):
    """
    Delete multiple documents from the 'Stores' collection based on the provided criteria.

    Args:
    - criteria (str): The criteria for deletion. Default is 'all' to delete all documents.

    Raises:
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
    try:
        # Establish a connection to the MongoDB server
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        if criteria.lower() == 'all':
            # Ask for confirmation before deleting all documents
            confirm_delete = input("Are you sure you want to delete all documents in the Stores collection? (y/n): ").lower()

            if confirm_delete == 'y':
                # Delete all documents in the collection
                result = await collection.delete_many({})

                # Log the result of the delete operation
                if result.deleted_count > 0:
                    delete_logger.info(f"{result.deleted_count} documents deleted successfully.")
                else:
                    delete_logger.warning("No documents found in the 'Stores' collection.")
            else:
                delete_logger.info("Deletion canceled. No documents were deleted.")
        else:
            delete_logger.warning("Invalid option. Please enter 'all' to delete all documents.")

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        delete_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        delete_logger.error(f"Unexpected error: {e}")

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            delete_logger.info("MongoDB client closed successfully.")
