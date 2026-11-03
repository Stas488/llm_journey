person = {'name':'Alex', 'age': 27, 'city': 'Moscow'}

print(person['name'])
person['age'] = 28
person['job'] = 'engineer'
print(person)

for key, value in person.items():
    print(f'{key}:{value}')

print(person.get('salary', 'not found'))

a = {1,2,3,4}
b = {3,4,5,6}
print(a|b) # объединит 2 множества
print(a&b) # пересечение 2 множеств
print(a-b) # разность

squares = [x**2 for x in range(5)]

print(squares)

evens = [x for x in range(100) if x%2==0]

print(evens)
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Задачи

s = 'hello world hello python world hello'
dict_of_words = {}
for word in s.split():
    if word not in dict_of_words:
        dict_of_words[word] = 1
    else:
        dict_of_words[word] +=1

print(dict_of_words)


result = sum(x for x in range(1,101) if x%2 ==0)
print(result)

list_of_nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
uniq_nums = list(set(list_of_nums))
uniq_nums.sort(reverse=True)
print(uniq_nums)

person = {'name': 'Alex', 'age': 27, 'city': 'Moscow'}

list_of_dict = [f'{key}={value}' for key, value in person.items()]

print(list_of_dict)

scores = {'Alex': 85, 'Bob': 92, 'Cara': 78, 'Dan': 95}

filtered = {key: value for key, value in scores.items() if value > 80}

print(filtered)