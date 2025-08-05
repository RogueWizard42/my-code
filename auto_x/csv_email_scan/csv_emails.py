# scanning emails froma csv file

import re
import csv

emails_only = []

with open ("employees.csv", "r") as file: #open the csv file
    reader = csv.reader(file) #read the file
    next(reader)  #skip the header
    for row in reader:
        if len(row) >= 2:
            emails = row[1] #get the emails from the second column
            if re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", emails): #match the emails using a regular expression pattern
                emails_only.append(emails) #store the emails in a list

print(emails_only)

# The code reads a csv file and extracts the emails from the file. It uses the re module to match the emails using a regular expression pattern. The emails are then stored in a list

