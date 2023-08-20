# Exim_mainlog_reader
Reads and interprets exim_mainlog for email troubleshooting


This Python script is designed to parse and convert Exim mail server log files into human-readable format. It reads the content of an exim_mainlog file, extracts relevant information from each log entry, and generates human-readable lines detailing the sender, recipient, timestamp, and subject of each email.

Requirements
Python 3.x
Usage
Place the exim_mainlog file in the same directory as the script.

Run the script by executing the following command in your terminal:
python exim_log_parser.py
The script will process the log file and display the parsed information on the screen.

Output
The script extracts details from each log entry, including:

Timestamp
Sender
Recipient
Subject
For each log entry, it generates a human-readable line in the following format:
At [timestamp], [sender] sent an email to [recipient] with subject '[subject]'.


You can choose between two ways to view the parsed log information:

Console Output: The parsed information will be printed to the console as it's processed.

File Output: If you'd like to save the parsed log information to a separate file, uncomment the section under "Alternatively, save the human-readable log to a new file" by removing the # at the beginning of each line. This will create a file named exim_mainlog_readable.txt in the same directory as the script, containing the human-readable log lines.

Example
For instance, if a log entry looks like this:
2023-08-20 10:30:15, sender@example.com, recipient@example.net, Subject: Hello, World!


The script will convert it to:
At 2023-08-20 10:30:15, sender@example.com sent an email to recipient@example.net with subject 'Hello, World!'.
