import re, pyperclip

# Create a regex for phone numbers
phoneNumRegex = re.compile(r'''
    # Optional area code
    (\d{3}|\(\d{3}\))?              # Area code, with or without parentheses
    (\s|-)?                         # Optional separator (space or dash)
    \d{3}                           # First 3 digits
    -                               # Dash separator
    \d{4}                           # Last 4 digits
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # Name before the @ symbol
    @ # At symbol
    [a-zA-Z0-9.-]+ # Domain name 
    (\.[a-zA-Z]{2,4}) # Top level domain
)''', re.VERBOSE)

# Find matches in the clipboard text
text = pyperclip.paste()


# Extract phone numbers and email addresses
extractedPhoneNumbers = phoneNumRegex.findall(text)
extractedEmailAddresses = emailRegex.findall(text)

print(extractedPhoneNumbers)
print(extractedEmailAddresses)