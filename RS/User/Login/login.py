import os
import logging
import bcrypt
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve MongoDB connection string from environment variables
uri = os.getenv("MONGO_CONNECTION_STRING")

# Initialize a logger for the login module
login_logger = logging.getLogger("login_logger")
login_logger.setLevel(logging.DEBUG)

async def login(username, password):
    """
    Attempt to log in a user.

    Parameters:
    - username (str): The username of the user.
    - password (str): The password entered by the user.

    Returns:
    - bool: True if login is successful, False otherwise.
    """
    # Connect to the UserInformation database
    client = AsyncIOMotorClient(uri)
    db = client["UserInformation"]
    collection = db["Users"]

    # Check if the username exists in the database
    user_data = await collection.find_one({"username": username})
    if user_data:
        # Check if the entered password matches the hashed password in the database
        hashed_password = user_data.get("password", "")
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
            # Log the successful login
            login_logger.info(f"User {username} successfully logged in.")
            return True
        else:
            login_logger.error("Incorrect password.")
    else:
        login_logger.error("Username not found.")

    # Close the database connection
    client.close()

    return False
