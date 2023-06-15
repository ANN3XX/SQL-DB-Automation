import pandas as pd
import sqlite3

# Define the path to the spreadsheet
spreadsheet_path = 'path/to/spreadsheet.xlsx'

# Define the SQLite database connection
database_path = 'path/to/database.db'
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Read the spreadsheet data using pandas
df = pd.read_excel(spreadsheet_path)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract the relevant data from the row
    column1_value = row['Column1']
    column2_value = row['Column2']
    # ...

    # Check if the record exists in the database based on a unique identifier
    select_query = f"SELECT * FROM your_table WHERE unique_id = '{column1_value}'"
    cursor.execute(select_query)
    existing_record = cursor.fetchone()

    if existing_record:
        # Update the existing record
        update_query = f"UPDATE your_table SET column2 = '{column2_value}' WHERE unique_id = '{column1_value}'"
        cursor.execute(update_query)
    else:
        # Insert a new record
        insert_query = f"INSERT INTO your_table (unique_id, column2) VALUES ('{column1_value}', '{column2_value}')"
        cursor.execute(insert_query)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
