# Welcome to My Ds Babel
***

## Task
The task of My Ds Babel is to provide a solution for data conversion between different formats, such as SQLite databases and CSV files.

## Description
My Ds Babel is a Python script that implements functions to convert data between SQLite databases and CSV files. It provides functionality to convert data from SQLite databases to CSV format and vice versa.

## Installation
There was no major installation but sqlite3 and csv was imported.

## Usage
The sql_to_csv(database, table_name):
Connects to the specified SQLite database and retrieves all rows from a specified table.
Extracts column names from the table.
Creates a CSV formatted string by combining column names and row values.
Returns the CSV string.

The csv_to_sql(csv_content, database, table_name):
Reads CSV data and determines column names and data types.
Constructs SQL statements to create a table with column definitions and insert values into the table.
Connects to the SQLite database, creates a table, and inserts the values.
Commits the changes and closes the connection.
```
./python my_ds_babel
```

### The Core Team
aniyom_e
deniran_o

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
