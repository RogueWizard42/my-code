Email Scan Automation 🕵️‍♂️📧

A script designed to hunt down specific email patterns—in this case, emails containing "old"—because sometimes, you need to separate the past from the present.

This automation extracts email addresses from a file, filters based on a keyword, and stores the results in a separate list. While this example focuses on "old", the logic can be easily modified to find any pattern you need (e.g., "new", "test", or `"suspicious" emails from that one sketchy coworker"**).
⚙️ How It Works

    Reads an input file containing a list of email addresses.
    Uses regex magic to extract only valid email addresses.
    Filters emails containing "old" (or any other keyword of your choosing).
    Outputs the extracted emails for further use (or exile).

📂 Setup & Usage
Prerequisites:

    A .txt file with a list of email addresses (not included in the repo because I just used a bunch of fake email addresses for testing).
    Python 3 installed on your system.

Running the Script:

    Place your email list file (fake_emails.txt) in the same directory as email_scan.py.
    Open a terminal and navigate to the email_scan folder:

cd path/to/email_scan

Run the script:

    python3 email_scan.py

    Profit. (Or at least get a clean list of filtered emails.)

🔍 Customization

If you want to filter emails based on a different keyword (instead of "old"), simply update this line in the script:

if "old" in email:  # Change "old" to whatever keyword you need

For example, to find all emails containing "test", modify it to:

if "test" in email:

This makes the script adaptable to different needs—whether you're sorting spam, flagging test emails, or just being nosy.
🔮 Future Enhancements

    Write the filtered emails to a new file instead of just printing them.
    Add user input to specify the keyword dynamically.
    Implement CLI arguments for better flexibility.

📜 License

This project is MIT-licensed, meaning you're free to use, modify, and share it—just don't blame me if you accidentally delete the wrong emails.
