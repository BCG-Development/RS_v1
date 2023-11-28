import bcrypt
import os
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the registration module
registration_logger = logging.getLogger("registration_logger")
registration_logger.setLevel(logging.DEBUG)

async def registration(username, password, confirm_password):
    """
    Register a new user.

    Parameters:
    - username (str): The username for the new user.
    - password (str): The password for the new user.
    - confirm_password (str): The confirmation of the password.

    Returns:
    - str: The ID of the newly registered user.
    """
    # Check if passwords match
    if password != confirm_password:
        registration_logger.error("Password and confirm password do not match.")
        raise ValueError("Password and confirm password do not match.")

    # Connect to the UserInformation database
    client = AsyncIOMotorClient(uri)
    db = client["UserInformation"]
    collection = db["Users"]

    # Check if the username already exists
    existing_user = await collection.find_one({"username": username})
    if existing_user:
        registration_logger.error("Username already exists.")
        raise ValueError("Username already exists. Please choose another username.")

    # Hash the password (Note: You should use a secure password hashing library)
    hashed_password = hash_password_function(password)

    # Insert the new user into the Users collection
    result = await collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    # Log the registration success
    registration_logger.info(f"User {username} successfully registered with ID: {result.inserted_id}")

    # Close the database connection
    client.close()

    return result.inserted_id

def hash_password_function(password):
    """
    Hash the given password using bcrypt.

    Parameters:
    - password (str): The password to be hashed.

    Returns:
    - str: The hashed password.
    """
    # Generate a salt and hash the password using bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")
