# CSV Email Extractor 📧

A simple Python script that reads a CSV file, extracts all valid email addresses using regular expressions, and prints them to the terminal.

---

## 🔍 What It Does

- Reads a file called `employees.csv` containing rows of employee data  
- Each row includes a name, email, and department  
- Uses the `csv` and `re` modules to:
  - Parse each row
  - Match and extract valid email addresses
- Stores all found emails in a list and prints them

---

## 📂 File Structure

- `csv_emails.py` — main script  
- `employees.csv` — sample CSV input file with 25 fake contacts  
- `.gitignore` — ignores unnecessary files (e.g., compiled `.pyc`, sample data)  
- `README.md` — this file  

---

## 🛠 How to Run

1. Ensure Python 3 is installed  
2. Clone the repo and `cd` into `csv_email_scan`  
3. Run the script:

```bash
python3 csv_emails.py
```
---

## ⚠️ Note on Sample Data

The included CSV uses fake, fictional names and addresses for practice and testing purposes.
Do not use real personal data in this project if pushing to a public repository.
---

## 🔮 Planned Enhancements

A follow-up version is planned that will:

    Write the extracted email addresses to a new .txt or .csv file

    Allow for different output formats (e.g., newline-delimited, comma-separated)

    Potentially include department-based filtering or summary stats
---
    
## 💡 Why This Exists

This project is part of a growing toolbox of small automation tools built in Python.
It lays the groundwork for more advanced CSV parsing, file handling, and data cleaning scripts.

    
