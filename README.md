# python_odbc

A Python program for accessing and querying data in a specific ODBC database.

## Files

- `main.py`: This is the entry point of the program. It calls the functions in the other files and executes them.
- `dbConn.py`: This file contains the connection information for the database. You will need to modify this file with your own connection details.
- `logicDatenzugriff.py`: This file contains all the functions that retrieve and display data from the database.

## Prerequisites

To use `python_odbc`, you will need to have the following dependencies installed:

- Python 3.7 or later
- pyodbc
- sqlalchemy

You will also need access to the database, including the necessary credentials and ODBC data source name.

## Running the program

To run the program, navigate to the root directory and run the following command:

```bash
python main.py
