import csv
import random
# Open the CSV file
with open('data.csv', 'r') as file:
    # Read the CSV content
    csv_data = list(csv.reader(file))
    row_count = sum(1 for _ in csv_data)
    print("This is the start csv file: ", csv_data)
    print("row count: ", row_count)

    random_row = random.randint(1, row_count)
    print("Random_row is: ", random_row)

    new_csv_file = csv_data.pop(random_row-1)
    print("this is the new csv file: ", csv_data)
