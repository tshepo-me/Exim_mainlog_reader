with open('exim_mainlog', 'r') as logfile:
    # Read the contents of the logfile into a string variable
    log_contents = logfile.read()
    # Split the logfile into individual lines
log_lines = log_contents.split('\n')

# Loop through each line of the logfile
for line in log_lines:
    # Parse the line to extract the relevant information
    # (e.g. timestamp, sender, recipient, etc.)
    # and then format the information into a human-readable string
    human_readable_line = f"At {timestamp}, {sender} sent an email to {recipient} with subject '{subject}'."
    # Print the human-readable log to the screen
for line in human_readable_lines:
    print(line)

# Alternatively, save the human-readable log to a new file
with open('exim_mainlog_readable.txt', 'w') as output_file:
    for line in human_readable_lines:
        output_file.write(line + '\n')