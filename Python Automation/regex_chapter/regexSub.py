import re

# This regex will match the first letter of the name and replace the rest with asterisks
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

print('----------------------------------')

# This regex will match the first letter of the name and replace the rest with asterisks
namesRegex = re.compile(r'Agent (\w)\w*') # Matches the first letter of the name
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')) # Replaces the name with the first letter and asterisks

print('----------------------------------')
