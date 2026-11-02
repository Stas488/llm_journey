nums = [10,20,30,40,50]

print('первый элемент:', nums[0])
print('последний элемент:', nums[-1])

print('срез с 0 элемента по 2', nums[:3])

print('срез с 2 элемента до конца', nums[2:])

nums.append(60) # добавляем в конец элемент 60

print(nums)

nums.pop() # удаляем последний элемент

nums.sort(reverse=True) # сортируем по убыванию

print(nums)

points = (3,7)

x,y = points

print(x,y)

# Задачи

arr = [5, 3, 8, 1, 9, 2]

print(arr[0])

print(arr[-1])

print(f'сумма всех элементов {sum(arr)}')

print(f'максимальный элемент в arr {max(arr)}')

print(f'минимальный элемент в arr {min(arr)}')

arr.sort()

print(arr)

print(arr[1:4])

films = ['клуб', "танцы", "песни", "лалаленд", "кент"]

films.append('Оппенгеймер')

films.pop(0)

print(films)