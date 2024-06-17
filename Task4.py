"""
Напишите скрипт-калькулятор, который принимает 3 аргумента:
1. первый аргумент
2. второй аргумент
3. операцию
и вычисляет результат
"""
import sys

match sys.argv[3]:
    case "+":
        print(int(sys.argv[1]) + int(sys.argv[2]))
    case "-":
        print(int(sys.argv[1]) - int(sys.argv[2]))
    case "*":
        print(int(sys.argv[1]) * int(sys.argv[2]))
    case "/":
        print(int(sys.argv[1]) / int(sys.argv[2]))
