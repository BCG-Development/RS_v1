import asyncio
from Logging.logging import setup_logging
from Database.Connection.ping_connection import connect_to_database
from Database.Delete.delete_docs import delete_one_document, delete_many_documents
from Database.InsertOne.insert_one import insert_document
from Database.InsertMany.insert_many import insert_documents

log_dir = r"RS\Logging\Loggers"

async def main():
    """
    Main function for the Route Solutions application.

    This function presents a menu to the user, allowing them to perform various operations
    related to inserting and deleting store information from a MongoDB database.

    Operations:
    1. Insert one store
    2. Insert many stores from Excel
    3. Delete one store by ID
    4. Delete many stores based on criteria or all to remove all stores
    """

    # Connect to the MongoDB database
    await connect_to_database()

    while True:
        try:
            print("Choose an option:")
            print("1. Insert one store")
            print("2. Insert many stores from Excel")
            print("3. Delete one store by ID")
            print("4. Delete many stores based on criteria or all to remove all stores")

            # Get user choice
            choice = input("Enter your choice (1, 2, 3, or 4): ")

            if not choice.isdigit() or choice not in ['1', '2', '3', '4']:
                raise ValueError("Invalid input. Please enter 1, 2, 3, or 4.")

            if choice == '1':
                # Insert one store
                id_value = input("Enter store ID: ")
                store_name_value = input("Enter store name: ")
                store_address_value = input("Enter store address: ")
                store_postcode_value = input("Enter store postcode: ")
                kms_value = float(input("Enter KMS: "))
                tail_lift_value = input("Does the store require a tail lift? (True/False): ").lower() == "true"

                await insert_document(
                    id=id_value,
                    store_name=store_name_value,
                    store_address=store_address_value,
                    store_postcode=store_postcode_value,
                    kms=kms_value,
                    tail_lift=tail_lift_value
                )

            elif choice == '2':
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

            elif choice == '3':
                # Delete one store by ID
                document_id = input("Enter the ID of the store to delete: ")
                delete_instance = delete_one_document()
                await delete_instance.delete_one_document(document_id)

            elif choice == '4':
                # Delete many stores based on criteria or all to remove all stores
                criteria_or_all = input("Enter 'all' to delete all stores or provide criteria for deletion: ")
                delete_instance = delete_many_documents()

                if criteria_or_all.lower() == 'all':
                    # Delete all documents in the "Stores" collection
                    await delete_instance
                else:
                    # Delete based on user-defined criteria
                    await delete_instance.delete_many_documents(criteria_or_all)
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

            # Ask the user if they want to input another operation
            another_operation = input("Do you want to perform another operation? (y/n): ").lower()
            if another_operation != 'y':
                break

        except ValueError as ve:
            print(f"Error: {ve}")
            continue

if __name__ == "__main__":
    # Set up logging
    setup_logging(log_dir)
    # Run the main function
    asyncio.run(main())
