import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter the URL: ")

# Read the data from the URL
data = urllib.request.urlopen(url).read()

# Parse the XML data
tree = ET.fromstring(data)

# Find all the <comment> tags
comments = tree.findall('comments/comment')

# Initialize the sum
total = 0

# Iterate through each <comment> tag
for comment in comments:
    # Find the <count> value
    count = comment.find('count').text
    # Add the count to the total
    total += int(count)

# Print the sum
print("Sum of <count> values:", total)