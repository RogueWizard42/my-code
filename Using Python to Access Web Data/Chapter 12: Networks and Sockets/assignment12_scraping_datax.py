import requests
from bs4 import BeautifulSoup

# Ask the user for a website
website = input("Enter a website URL: ")

# Send a GET request to the website
response = requests.get(website)

# Parse the HTML content of the website
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <span> tags
span_tags = soup.find_all('span')

# Initialize a variable to store the sum of numbers
total_sum = 0

# Iterate over the <span> tags and extract the text content
for span in span_tags:
    try:
        # Convert the text content to an integer and add it to the total sum
        total_sum += int(span.text)
    except ValueError:
        # Ignore any non-integer values
        pass

# Print the result
print("Sum of numbers:", total_sum)