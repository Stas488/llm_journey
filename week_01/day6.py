import json
from datetime import datetime

# Задача 1
list_of_lines = []

with open('week_01/students.csv', 'r', encoding='utf-8') as f:
    next(f)
    summa = 0
    count = 0
    for line in f:
        summa+=int(line.strip().split(',')[-1])
        count+=1
    mean_grade = summa/count
print(mean_grade)

# Задача 2

data = [{'name':'Alex','age':27,'grade':85}, 
       {'name':"Bob",'age':22,'grade':92}, 
       {'name':"Cara",'age':25,'grade':78}, 
       {'name':"Dan",'age':24,'grade':88}]

with open('data.json', 'w', encoding='utf-8', ) as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open('data.json', 'r', encoding='utf-8') as f:
    file = json.load(f)

print(file[0])
print(file[1])


# Задача 3


def load_config(path):
    '''Читает файл конфига json -> на выходе словарь'''
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


try:
    res1 = load_config('week_01/config.json')
    print(f'успех: lr = {res1["lr"]}')
except FileNotFoundError as e:
    print(f'FileNotFoundError: {e}')
except ValueError as e:
    print(f'ValueError: {e}')


try:
    res2 = load_config('week_01/nope.json')
except FileNotFoundError as e:
    print(f'FileNotFoundError: {e}')
except ValueError as e:
    print(f'ValueError: {e}')

try:
    res3 = load_config('week_01/bad.json')
except FileNotFoundError as e:
    print(f'FileNotFoundError: {e}')
except ValueError as e:
    print(f'ValueError: {e}')


def log(message, path = 'app.log'):
    '''Пишет лог в файл {path} '''
    with open(path, 'a') as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: {message}\n')



log('модель загружена')
log('начато обучение')
log('обучение завершено')

with open('app.log', 'r') as f:
    for line in f:
        print(line)