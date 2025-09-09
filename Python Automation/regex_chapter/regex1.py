import re

message = 'Call me at (82) 98873-1513 tomorrow, or at (11) 98810-1020 for my office line.'

phoneNumRegex = re.compile(r'\(\d{2}\)\s9\d{4}-\d{4}')
print(phoneNumRegex.findall(message))