import csv

# Define the data for the CSV file
data = [
    ["How are you today?", "Yes", 5],
    ["Did you enjoy the movie?", "No", 8],
    ["Have you been to this restaurant before?", "Yes", 2],
    ["Is it raining outside?", "No", 6],
    ["Did you like the book you read?", "Yes", 9],
    ["Are you planning to travel this summer?", "Yes", 4],
    ["Have you ever tried bungee jumping?", "No", 7],
    ["Do you prefer coffee or tea?", "Tea", 3],
    ["Have you watched the latest episode of your favorite TV show?", "Yes", 1],
    ["Did you finish reading the book?", "No", 10],
    ["Are you a morning person?", "Yes", 5],
    ["Have you visited any art galleries recently?", "No", 8],
    ["Did you try any new recipes lately?", "Yes", 2],
    ["Do you enjoy outdoor activities?", "No", 6],
    ["Did you attend any concerts in the past month?", "Yes", 9],
    ["Have you ever been scuba diving?", "Yes", 4],
    ["Do you like spicy food?", "No", 7],
    ["Have you been practicing any musical instruments?", "Yes", 3],
    ["Did you go for a walk today?", "No", 1],
    ["Are you excited about the upcoming event?", "Yes", 10],   [
        "Have you visited a museum recently?", "Yes", 5],
    ["Did you try any new restaurants this week?", "No", 8],
    ["Are you currently reading a book?", "Yes", 2],
    ["Do you enjoy gardening?", "No", 6],
    ["Have you ever gone skydiving?", "Yes", 9],
    ["Do you prefer sweet or savory food?", "Sweet", 4],
    ["Have you attended any virtual events recently?", "Yes", 7],
    ["Did you watch a new movie this month?", "No", 3],
    ["Are you a fan of sports?", "Yes", 1],
    ["Did you take any photographs today?", "No", 10]
]

# Specify the filename for the CSV file
filename = "questions.csv"

# Write data to the CSV file
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer", "Number"])  # Write the header row

    for line in data:
        writer.writerow(line)  # Write each line of data
