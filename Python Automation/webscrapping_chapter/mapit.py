import webbrowser, sys, pyperclip

sys.argv

#check if command line arguments are provided
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) # Join the command line arguments into a single string
else:
    address = pyperclip.paste()

# Use the webbrowser module to open the address in Google Maps
webbrowser.open('https://www.google.com/maps/place/' + address)