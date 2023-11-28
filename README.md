# Route Solutions

**Route Solutions** is a software solution designed for managing and organizing store information. This application facilitates tasks such as inserting individual stores, importing multiple stores from Excel files, efficiently deleting store records based on specified criteria, removing all stores, searching for stores by ID, and modifying store restrictions.

## Functionality Overview

### Inserting Stores

The application allows users to add individual stores by providing store-specific details such as ID, name, address, postcode, kilometers, and whether the store requires a tail lift. Additionally, users can specify store restrictions for each day of the week.

### Bulk Insertion from Excel

Users can streamline the process by importing multiple stores from an Excel file. The application parses the file, validates the data, and inserts each store into the database.

### Deleting Stores

There are options to delete stores based on specific criteria or remove all stores. Users can delete a single store by providing its ID or choose to delete multiple stores by specifying criteria, such as all stores requiring a tail lift.

### Searching for Stores

Users can search for a store by providing its ID. The application retrieves and displays information for the specified store if it exists. Additionally, users can search for all stores and view their store restrictions.

### Modifying Store Restrictions

Users can modify the store restrictions for an existing store by providing the store ID and updating the opening hours for each day of the week.

### Logging

The application utilizes logging to capture and record events during database interactions, including successful document insertions, deletions, searches, modifications, and potential errors.

## Logging

The application logs important events and errors during database interactions. Separate loggers are used for different modules, including connection, deletion, insertion, modification, and search. This ensures a detailed record of activities and aids in troubleshooting.

## Database Structure

The application operates on a MongoDB database named “StoreInformation” with a collection named “Stores.” Each document in the collection represents a store and includes fields such as ID, store name, address, postcode, kilometers, tail lift requirement, and store restrictions.

## Project Structure

The project is organized into distinct modules for connection handling, insertion, deletion, searching, modification, and logging. The structure promotes code readability, maintainability, and the ease of extending functionality.

## Installation

Follow these steps to set up Route Solutions:

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/your-username/route-solutions.git
    ```

2. Navigate to the project directory.

    ```bash
    cd route-solutions
    ```

3. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the MongoDB connection string.

    - Create a `.env` file in the project root.
    - Add your MongoDB connection string as follows:

        ```dotenv
        MONGO_CONNECTION_STRING=your_connection_string
        ```

## Usage

Explore the functionalities provided by Route Solutions:

- Insert one store
- Insert many stores from an Excel file
- Delete one store by ID
- Delete many stores based on criteria or all to remove all stores
- Search for a store by ID
- Search for all stores
- Modify store restrictions for an existing store

Refer to the application structure and logging details in the previous sections for insights into its inner workings.

Now you’re ready to interact with Route Solutions. Head to the [Getting Started](#installation) section to run the application.

## Contributing

If you’re interested in contributing to Route Solutions, feel free to:

1. Fork the repository.
2. Create your feature branch:

    ```bash
    git checkout -b feature/YourFeature
    ```

3. Commit your changes:

    ```bash
    git commit -m “Add YourFeature”
    ```

4. Push the branch:

    ```bash
    git push origin feature/YourFeature
    ```

5. Open a pull request, and we’ll review your contribution.

## License

Route Solutions is licensed under the [Apache License 2.0](LICENSE). See the [LICENSE](LICENSE) file for more details.
