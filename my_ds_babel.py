import sqlite3
import csv


def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)  # Connect to the SQLite database
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")  # Fetch all rows from the table
    rows = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({table_name})")  # Fetch column names
    columns = [column[1] for column in cursor.fetchall()]

    csv_string = ','.join(columns) + '\n'  # Create a CSV formatted string with column names
    for row in rows[1:]:
        csv_string += ','.join(map(str, row)) + '\n'  # Append rows to the CSV string

    conn.close()
    return csv_string


def csv_to_sql(csv_content, database, table_name):
    clean = [each.replace("\n", "") for each in csv_content.readlines()]

    header = clean[0].split(",")  # Get the header
    dtype = []
    body = clean[1].split(',')
    for i in range(len(body)):  # Determine data types of columns
        if body[i].isdigit():
            dtype.append('INTEGER')
        else:
            try:
                float(body[i])
                dtype.append('FLOAT')
            except:
                dtype.append('TEXT')

    word_map = ", ".join([f"[{header[x]}] {dtype[x]}" for x in range(len(body))])  # Create column definitions

    main_string = ""
    for each in clean[1:]:
        new_texts = []
        texts = each.split(",")
        for x in range(len(texts)):
            if dtype[x] == 'TEXT':
                if "'" in texts[x]:
                    texts[x] = texts[x].replace("'", "")
                new_texts.append(f"'{texts[x]}'")
            else:
                new_texts.append(texts[x])
        main_string += "(" + ",".join(new_texts) + "), "

    connect = sqlite3.connect(database)  # Connect to the SQLite database
    cursor = connect.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name};")  # Create table and columns
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({word_map});")
    cursor.execute(f"INSERT INTO {table_name} VALUES {main_string[:-2]}")  # Insert values into the table

    connect.commit()  # Commit the changes
    connect.close()


# Test to convert SQL to CSV
list_fault_lines = sql_to_csv("all_fault_line.db", "fault_lines")
file = open("list_fault_lines.csv", "w", encoding='utf-8')  # Open the CSV file in write mode
file.write(list_fault_lines)  # Write the CSV data
file.close()  # Close the CSV file

# Test to convert CSV to SQL
csv_content = open("list_volcano.csv")  # Open the CSV file
csv_to_sql(csv_content, 'list_volcanos.db', 'volcanos')  # Convert CSV to SQL and store in a SQLite database
csv_content.close()  # Close the CSV file