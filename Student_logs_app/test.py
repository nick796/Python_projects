import openpyxl
import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Execute SQL query to retrieve data
cursor.execute("SELECT * FROM students")

# Fetch all records
records = cursor.fetchall()

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write the column headers to the first row of the sheet
column_names = [column[0] for column in cursor.description]
sheet.append(column_names)

# Write the data to the sheet
for record in records:
    sheet.append(record)

# Save the workbook
workbook.save("output.xlsx")

# Close the database connection
conn.close()
