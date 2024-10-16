import os
import time

# print(os.getcwd())

if os.path.exists('directory'):
    os.chdir('directory')
else:
    os.mkdir('directory')
    os.chdir('directory')

print(os.getcwd())

path = r'C:\Users\User\PycharmProjects\pythonProject'

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m/%Y %H:%M', time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(path)
        print(f'Обнаружен файл: {file}; Путь: {filepath}; Размер: {filesize} байт; Время изменения: {formatted_time};\n'
              f'Родительская директория: {parent_dir}')
