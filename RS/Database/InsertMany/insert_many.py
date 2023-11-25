import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError
import logging
import pandas as pd

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the insert_many module
insert_many_logger = logging.getLogger("insert_many_logger")
insert_many_logger.setLevel(logging.DEBUG)

async def insert_documents(file_path):
    """
    Insert multiple documents into the 'Stores' collection based on data from an Excel file.

    Args:
    - file_path (str): The path to the Excel file containing store information.

    Raises:
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
    try:
        # Establish a connection to the MongoDB server
        client = AsyncIOMotorClient(uri)
        db = client["StoreInformation"]
        collection = db["Stores"]

        # Read data from the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Iterate over each row in the DataFrame and insert documents
        for _, row in df.iterrows():
            await _validate_and_insert(collection, row)

    except PyMongoError as pe:
        # Log MongoDB-specific errors
        insert_many_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        insert_many_logger.error(f"Unexpected error: {e}")

    finally:
        # Close the MongoDB client and log closure attempt
        if client:
            client.close()
            insert_many_logger.info("MongoDB client closed successfully.")

async def _validate_and_insert(collection, row):
    """
    Validate and insert a single document into the 'Stores' collection.

    Args:
    - collection: The MongoDB collection to insert the document into.
    - row (pd.Series): A row from the DataFrame containing store information.

    Raises:
    - ValueError: If a validation error occurs, such as a missing column.
    - PyMongoError: If an error occurs during the MongoDB operation.
    - Exception: For unexpected errors during the process.
    """
    try:
        # Validate that the 'Tail Lift' column is present in the row
        if 'Tail Lift' not in row:
            raise ValueError("Column 'Tail Lift' not found in the row.")

        # Extract values from the row and create a document
        tail_lift = bool(row["Tail Lift"])
        document = {
            "_id": row["ID"],
            "Store name": row["Store Name"],
            "Store Address": row["Store Address"],
            "Store Postcode": row["Store Postcode"],
            "Kilometers": row["Kilometers"],
            "Does the store require a tail lift? (True/False)": tail_lift
        }

        # Insert the document into the collection and log the result
        result = await collection.insert_one(document)
        insert_many_logger.info(f"Document inserted with ID: {result.inserted_id}")

    except ValueError as ve:
        # Log validation errors
        insert_many_logger.error(f"Validation error: {ve}")
    except PyMongoError as pe:
        # Log MongoDB-specific errors
        insert_many_logger.error(f"MongoDB error: {pe}")
    except Exception as e:
        # Log unexpected errors
        insert_many_logger.error(f"Unexpected error: {e}")
