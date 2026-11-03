# 1. Простая функция
def add(a, b):
    return a + b

print(add(2, 3))

# 2. Значение по умолчанию
def greet(name='world'):
    return f'Hello, {name}!'

print(greet())
print(greet('Alex'))

def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4))
print(total())

def describe(**info):
    for key, value in info.items():
        print(f'{key}: {value}')

describe(name='Alex', age=27, city='Moscow')


try:
    int('abc')
except ValueError:
    print('не превращается в число')

try:
    result = 10 / 0
except ZeroDivisionError:
    print('на ноль делить нельзя')
finally:
    print('этот блок выполнится всегда')

def withdraw(balance, amount):
    if balance<amount:
        raise ValueError('Недостаточно средств')
    return balance - amount

try:
    withdraw(100, 200)
except ValueError as e:
    print(f'Ошибка: {e}')


# Задачи

def calculate_bmi(weight, height):
    if weight<=0 or height<=0:
        raise ValueError('вес и рост должны быть положительными')
    return weight/height**2

try:
    res = calculate_bmi(-1, -5)
except ValueError as e:
    print(f'Ошибка вызова функции: {e}')


def max_of(*args):
    if not args:
        raise ValueError('нужен хотя бы один аргумент')
    maximum = args[0]
    for i in args:
        if maximum<i:
            maximum = i
    return maximum

print(max_of(3, 7, 1, 9, 4))


def train_model(**config):
    for key, value in config.items():
        print(f'{key}: {value}')

train_model(lr=0.01, epochs=10, batch_size=32)


def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('аргументы должны быть числами')
    if b == 0:
        raise ZeroDivisionError('деление на ноль')
    return a / b

# успех
print(safe_divide(1, 2))          # 0.5

# деление на ноль
try:
    safe_divide(1, 0)
except ZeroDivisionError as e:
    print(f'ZeroDivisionError: {e}')

# не число
try:
    safe_divide('1', 2)
except TypeError as e:
    print(f'TypeError: {e}')