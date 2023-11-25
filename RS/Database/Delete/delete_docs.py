import os
from bson import ObjectId
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

load_dotenv()

uri = os.getenv("MONGO_CONNECTION_STRING")

delete_logger = logging.getLogger("delete_logger")
delete_logger.setLevel(logging.DEBUG)

async def delete_one_document(document_id):
    try:
        delete_logger.info("Searching for document.....")
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]
        
        try:
            document_id = ObjectId(document_id)
        except Exception as e:
            pass
        
        if isinstance(document_id, ObjectId):
            filter_query = {"_id": document_id}
        else:
            filter_query = {"_id": int(document_id)}
            
        result = await collection.delete_one(filter_query)
        
        if result.deleted_count == 1:
            delete_logger.info(f"Document with ID {document_id} deleted successfully.")
        else:
            delete_logger.warning(f"No document found with ID {document_id}.")
            
    except PyMongoError as pe:
        delete_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        delete_logger.error(f"Unexpected error: {e}")
        
    finally:
        if client:
                client.close()
                delete_logger.info("MongoDB client closed successfully.")
                
async def delete_many_documents(criteria='all'):
    try:
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        if criteria.lower() == 'all':
            # Ask for confirmation before deleting all documents
            confirm_delete = input("Are you sure you want to delete all documents in the Stores collection? (y/n): ").lower()

            if confirm_delete == 'y':
                # Delete all documents in the collection
                result = await collection.delete_many({})

                if result.deleted_count > 0:
                    delete_logger.info(f"{result.deleted_count} documents deleted successfully.")
                else:
                    delete_logger.warning("No documents found in the 'Stores' collection.")
            else:
                delete_logger.info("Deletion canceled. No documents were deleted.")
        else:
            delete_logger.warning("Invalid option. Please enter 'all' to delete all documents.")

    except PyMongoError as pe:
        delete_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        delete_logger.error(f"Unexpected error: {e}")

    finally:
        if client:
            client.close()
            delete_logger.info("MongoDB client closed successfully.")