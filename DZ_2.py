#Задача 10:Определить количество монеток, которе надо перевернуть

# print('Введите общее количество монет: ')
# n = int(input())
# count1 = 0
# count2 = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count1 += 1
#     else:
#         count2 += 1

#         if count1 > count2:
#             print(count1)
#         else:
#             print(count2)

# задача Найти значение загаданных чисел
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)
#         else:
#             print("Какая-то фигня получается!")

# Задача: Ввести все целые степени 2-ки, не превосходящие числа N
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i +=1