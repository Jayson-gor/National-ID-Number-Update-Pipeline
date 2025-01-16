# National-ID-Number-Update-Pipeline
This project involves updating the NATIONAL_ID_NUMBER field in an existing PostgreSQL database from values stored in an Excel file. The script performs an efficient batch update to correct truncated national ID numbers without altering existing database relationships or removing records.

## Tools and Technologies Used:
1. Database Management: PostgreSQL
2. Scripting Language: Python
3. Libraries:
         - pandas for reading and processing Excel files
         - psycopg2 for PostgreSQL database interactions
4. Version Control: GitHub

## Project Workflow:
i. Data Source (Excel File):
Reads national ID numbers from an Excel sheet.

ii. Data Processing:
Converts the Excel data into a dictionary for quick lookups.

iii. Database Connection:
Establishes connection to the PostgreSQL database.

iv. Batch Update:
Uses execute_batch from psycopg2.extras for efficient updates.

v. Error Handling:
Implements transaction rollback in case of errors during updates.


## Key Components:
SQL Query: Updates the dependants_payroll table's NATIONAL_ID_NUMBER based on DEPENDANT_CODE.
Error Management: Ensures data integrity by rolling back changes if an error occurs.

## Challenges:
1. Ensuring that updates do not disrupt existing database relationships.
2. Managing the conversion of data types (from int to string for national ID numbers).

## Solution:
The script leverages dictionaries for mapping and batch processing for performance, ensuring only necessary records are updated without affecting the broader database schema.

## Deployment Notes:
Replace placeholder database credentials with actual credentials when deploying.
Ensure the Excel file path is correct for your environment.
