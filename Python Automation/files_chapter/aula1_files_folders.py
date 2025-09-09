import os

print(os.listdir('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation'))

totalsize = 0

for filename in os.listdir('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation\\regex_chapter'):
    if filename.endswith('.py'):
        filepath = os.path.join('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation\\regex_chapter', filename)
        totalsize += os.path.getsize(filepath)

for filename in os.listdir('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation\\files_chapter'):
    if filename.endswith('.py'):
        filepath = os.path.join('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation\\files_chapter', filename)
        totalsize += os.path.getsize(filepath)

print(f'Total size of .py files: {totalsize} bytes')


# Creates a new folder if it doesn't exist
os.makedirs('C:\\Users\\LENOVO\\OneDrive\\Área de Trabalho\\Python Automation\\new_folder', exist_ok=True)