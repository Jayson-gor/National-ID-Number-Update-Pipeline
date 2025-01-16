import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# Database connection parameters
conn = psycopg2.connect(
    host="your_host",  
    port=5432,  
    database="your_database",  
    user="your_username",  
    password="your_password"  
)
cursor = conn.cursor()

# Load the Excel file
file_path = "path_to_your_file.xlsx"
dependant_details = pd.read_excel(file_path, sheet_name="Sheet1", dtype={'NATIONAL_ID_NUMBER': str})

# Prepare a dictionary of updates: {DEPENDANT_CODE: NATIONAL_ID_NUMBER}
updates = dependant_details.set_index('DEPENDANT_CODE')['NATIONAL_ID_NUMBER'].to_dict()

# Batch update SQL query
update_query = """
    UPDATE dependants_payroll
    SET NATIONAL_ID_NUMBER = %s
    WHERE DEPENDANT_CODE = %s;
"""

# Convert the dictionary to a list of tuples for batch processing
update_values = [(national_id, dependant_code) for dependant_code, national_id in updates.items()]

try:
    # Execute the batch update
    execute_batch(cursor, update_query, update_values)
    
    # Commit the transaction
    conn.commit()
    print(f"Successfully updated {cursor.rowcount} records.")
except Exception as e:
    # Rollback if something goes wrong
    conn.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
