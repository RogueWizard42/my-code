# simple email scanner using regex - looking for old emails in a list of emails

import re


old_emails = []

with open("fake_emails.txt", "r") as file:
    content = file.read()
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, content)
    
    
for email in emails:   
    if "old" in email:
        old_emails.append(email)
        
print(old_emails) 



    
    
    