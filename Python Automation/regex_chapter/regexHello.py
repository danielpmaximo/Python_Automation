import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.findall('Hello world!'))
print(beginsWithHello.findall('He said "Hello"'))

endsWithWorld = re.compile(r'world!$')
print(endsWithWorld.findall('Hello world!'))
print(endsWithWorld.findall('Hello world! How are you?'))

allDigits = re.compile(r'^\d+$') # Matches only digits
print(allDigits.findall('1234567890'))
print(allDigits.findall('1234567890x123'))
print(allDigits.findall('1234567890abc'))

atRegex = re.compile(r'.at') # Matches any character followed by 'at'
print(atRegex.findall('the cat in the hat sat on the mat of the flat'))

firstNameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(firstNameRegex.findall('First Name: Alice Last Name: Smith'))