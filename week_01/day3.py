
x = 15
if x > 0:
    print('положительное')
elif x == 0:
    print('ноль')
else:
    print('отрицательное')


age = 25
if age >= 18 and age < 65:
    print('взрослый трудоспособный')


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

n = 3
while n > 0:
    print(n)
    n = n - 1


for i in range(10):
    if i == 5:
        break
    print(i)   # 0,1,2,3,4

# 7. continue
for i in range(5):
    if i % 2 == 0:
        continue
    print(i)   # 1, 3

# Задачи

for i in range(1,21):
    if i%15 == 0:
        print('FizzBuzz')
    elif i%3 ==0:
        print('Fizz')
    elif i%5 ==0:
        print('Buzz')
    else:
        print(i)

sum = 0
for i in range(1, 101):
    if i%2 == 0:
        sum+=i
print(f'сумма всех чётных чисел равна {sum}')


arr = [3, 7, 1, 9, 4, 8]
target= 9

for i in range(len(arr)):
    if arr[i] == target:
        print(f'нашли на позиции: {i}')


s = 'hello world'
target = 'l'
count = 0
for i in s:
    if i == 'l':
        count+=1
print(f'Количесвто букв {target} равно {count}')