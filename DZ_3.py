# Задача 16: Подсчитать сколько раз встречается число 
#print(len(set(list_dialects)))

# n = int(input())
# lst = []
# for i in range(n):
    
#     num = int(input())
#     lst.append(num)

#     count = 0
       
#     if lst[i] == num:
#         count = count + 1
# print(count)

# Задача 18: Найти самое близекое значение к заданнму числу Х

n = int(input())
lst = []
for i in range(n):
    
    num = int(input())
    lst.append(num)

    x = (int(input("Ввести число х: ")))
    min = abs(x - 1)
    index = 0
    for i in range(1, n):
        count = abs(x - 1)
        if count < min:
            min = count
            index = i
    print(min)







