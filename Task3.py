"""
Напишите скрипт который принимает 2 аргумента и записывает 
первый аргумент в файл где имя файла второй аргумент.
"""
import sys

data = sys.argv[1]
filename = sys.argv[2]

with open(filename, "w") as file:
    file.write(data)