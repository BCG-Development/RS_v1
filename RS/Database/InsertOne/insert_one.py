import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the insert_one module
insert_one_logger = logging.getLogger("insert_one_logger")
insert_one_logger.setLevel(logging.DEBUG)

def validate_tail_lift(tail_lift):
    """
    Validate the tail_lift parameter.

    Args:
    - tail_lift: The tail lift parameter to be validated.

    Returns:
    - bool: True if the validation is successful, False otherwise.

    Raises:
    - ValueError: If the input for tail lift is not a boolean.
    """
    try:
        if not isinstance(tail_lift, bool):
            raise ValueError("Invalid input for tail lift. Please enter True or False.")
    except ValueError as ve:
        insert_one_logger.error(f"Validation error: {ve}")
        return False
    return True

async def insert_document(id, store_name, store_address, store_postcode, kms, tail_lift):
    """
    Insert a single document into the 'Stores' collection.

    Args:
    - id: The ID of the store.
    - store_name: The name of the store.
    - store_address: The address of the store.
    - store_postcode: The postcode of the store.
    - kms: The kilometers value.
    - tail_lift: The tail lift requirement (True or False).

    Raises:
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
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
        # Log MongoDB-specific errors
        insert_one_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        insert_one_logger.error(f"Unexpected error: {e}")

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            insert_one_logger.info("MongoDB client closed successfully.")
