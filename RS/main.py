import asyncio
from Logging.logging import setup_logging
from Database.Connection.ping_connection import connect_to_database
from Database.Delete.delete_docs import delete_one_document, delete_many_documents
from Database.InsertOne.insert_one import insert_document
from Database.InsertMany.insert_many import insert_documents
from Database.SearchOne.search_one import search_one
from Database.SearchAll.search_all import search_all
from Database.Modify.modify import modify_document
from User.Registration.register import registration
from User.Login.login import login

log_dir = r"RS\Logging\Loggers"

async def main():
    """
    Main function for the Route Solutions application.

    This function presents a menu to the user, allowing them to perform various operations
    related to inserting, deleting, searching, and modifying store information from a MongoDB database.

    Operations:
    1. Register
    2. Login
    -----------------------
    3. Insert one store
    4. Insert many stores from Excel
    5. Delete one store by ID
    6. Delete many stores based on criteria or all to remove all stores
    7. Search for a store by ID
    8. Search for all stores
    9. Modify store restrictions for an existing store  # Added new option
    """

    # Connect to the MongoDB database
    await connect_to_database()
    
    is_user_logged_in = False

    while True:
        try:
            if not is_user_logged_in:
                # Show registration and login options
                print("Choose an option:")
                print("1. Register")
                print("2. Login")

                # Get user choice
                choice = input("Enter your choice (1 or 2): ")

                if choice == '1':
                    # Register a new user
                    username = input("Enter your username: ")
                    password = input("Enter your password: ")
                    confirm_password = input("Confirm your password: ")
                    try:
                        await registration(username, password, confirm_password)
                        print("Registration successful. Please login.")
                    except ValueError as ve:
                        print(f"Registration error: {ve}")

                elif choice == '2':
                    # Login
                    login_attempts = 0
                    while login_attempts < 3:  # Allow three login attempts
                        username = input("Enter your username: ")
                        password = input("Enter your password: ")
                        if await login(username, password):
                            print("Login successful. You can now access options 3 to 9.")
                            is_user_logged_in = True
                            break
                        else:
                            login_attempts += 1
                            print(f"Invalid credentials. Remaining attempts: {3 - login_attempts}")

                    if login_attempts == 3:
                        print("Too many unsuccessful login attempts. Exiting.")
                        break
                        
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            else:
                # Show options for logged-in users
                print("Choose an option:")
                print("3. Insert one store")
                print("4. Insert many stores from Excel")
                print("5. Delete one store by ID")
                print("6. Delete many stores based on criteria or all to remove all stores")
                print("7. Search for a store by ID")
                print("8. Search for all stores")
                print("9. Modify store restrictions for an existing store")
                print("10. Exit")

                # Get user choice
                choice = input("Enter your choice (3 to 10): ")

                if not choice.isdigit() or choice not in ['3', '4', '5', '6', '7', '8', '9', '10']:
                    raise ValueError("Invalid input. Please enter a number between 3 and 10.")

                if choice == '3':
                    # Insert one store
                    id_value = input("Enter store ID: ")
                    store_name_value = input("Enter store name: ")
                    store_address_value = input("Enter store address: ")
                    store_postcode_value = input("Enter store postcode: ")
                    kms_value = float(input("Enter KMS: "))
                    tail_lift_value = input("Does the store require a tail lift? (True/False): ").lower() == "true"
                    store_restrictions = {}
                    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                        opening_hours = input(f"Enter opening hours for {day} (e.g., 09:00 AM - 05:00 PM): ")
                        store_restrictions[day] = opening_hours

                    await insert_document(
                        id=id_value,
                        store_name=store_name_value,
                        store_address=store_address_value,
                        store_postcode=store_postcode_value,
                        kms=kms_value,
                        tail_lift=tail_lift_value,
                        store_restrictions=store_restrictions
                    )

                elif choice == '4':
                    # Insert many stores from Excel
                    # Get file path for Excel file
                    file_path = input("Enter the path to the Excel file: ")

                    try:
                        # Create an instance of InsertMany using the file path
                        await insert_documents(file_path)

                    except FileNotFoundError as e:
                        print(f"File not found: {file_path}")
                    except PermissionError as e:
                        print(f"Permission error: {e}")
                    except Exception as e:
                        print(f"Unexpected error: {e}")

                elif choice == '5':
                    # Delete one store by ID
                    document_id = input("Enter the ID of the store to delete: ")
                    await delete_one_document(document_id)

                elif choice == '6':
                    # Delete many stores based on criteria or all to remove all stores
                    criteria_or_all = input("Enter 'all' to delete all stores or provide criteria for deletion: ")
                    delete_instance = delete_many_documents()

                    if criteria_or_all.lower() == 'all':
                        # Delete all documents in the "Stores" collection
                        await delete_instance
                    else:
                        # Delete based on user-defined criteria
                        await delete_instance.delete_many_documents(criteria_or_all)

                elif choice == '7':
                    # Search for a store by ID
                    document_id = input("Enter the ID of the store to search: ")
                    result = await search_one(document_id)
                    if result:
                        print("-" * 30)
                        print("Store found:")
                        print(f"Store ID: {result['_id']}")
                        print(f"Store Name: {result['Store name']}")
                        print(f"Store Address: {result['Store Address']}")
                        print(f"Store Postcode: {result['Store Postcode']}")
                        print(f"Kilometers: {result['Kilometers']}")
                        print(f"Does the store require a tail lift? {result['Does the store require a tail lift? (True/False)']}")
                        
                        # Print Store Restrictions if present
                        store_restrictions = result.get('Store Restrictions', {})
                        if store_restrictions:
                            print("Store Restrictions:")
                            for day, hours in store_restrictions.items():
                                print(f"{day}: {hours}")
                        
                        print("-" * 30)
                    else:
                        print(f"No store found with ID: {document_id}")

                elif choice == '8':
                    # Search for all stores
                    results = await search_all()
                    if results:
                        print("-" * 30)
                        print("All stores found:")
                        for store in results:
                            print(f"Store ID: {store['_id']}")
                            print(f"Store Name: {store['Store name']}")
                            print(f"Store Address: {store['Store Address']}")
                            print(f"Store Postcode: {store['Store Postcode']}")
                            print(f"Kilometers: {store['Kilometers']}")
                            print(f"Does the store require a tail lift? {store['Does the store require a tail lift? (True/False)']}")
                            
                            # Print Store Restrictions if present
                            store_restrictions = store.get('Store Restrictions', {})
                            if store_restrictions:
                                print("Store Restrictions:")
                                for day, hours in store_restrictions.items():
                                    print(f"{day}: {hours}")
                            
                            print("-" * 30)
                    else:
                        print("No stores found.")

                elif choice == '9':
                    # Modify store restrictions
                    document_id = input("Enter the ID of the store to modify: ")
                    store_restrictions = {}
                    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                        opening_hours = input(f"Enter opening hours for {day} (e.g., 09:00 AM - 05:00 PM): ")
                        store_restrictions[day] = opening_hours

                    try:
                        await modify_document(
                            document_id=document_id,
                            store_restrictions=store_restrictions
                        )
                    except Exception as e:
                        print(f"An error occurred: {e}")

                elif choice == '10':
                    # Exit the program
                    break

                else:
                    print("Invalid choice. Please enter a number between 3 and 10.")

        except ValueError as ve:
            print(f"Error: {ve}")
            continue

if __name__ == "__main__":
    # Set up logging
    setup_logging(log_dir)
    # Run the main function
    asyncio.run(main())
