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

# n = int(input())
# lst = []
# for i in range(n):
    
#     num = int(input())
#     lst.append(num)

#     x = (int(input("Ввести число х: ")))
#     min = abs(x - 1)
#     index = 0
#     for i in range(1, n):
#         count = abs(x - 1)
#         if count < min:
#             min = count
#             index = i
#     print(min)

# Задача
print('Введите слово на кирилице: ')
s = str(input())
print('ИЛИ на латинице: ')
i = str(input())

dictionary_1 = {
    1:'AEIOULNSTR',
    2:'DG',
    3:'BCMP',
    4:'FHVWY',
    5:'K',
    8:'JX',
    10:'QZ'
}
dictionary_2 = {
    1:'АВЕИНОРСТ',
    2:'ДКЛМПУ',
    3:'БГЁЬЯ',
    4:'ЙЫ',
    5:'ЖЗХЦЧ',
    8:'ШЭД',
    10:'ФЩЪ'
}

result_1 = [key for letter in s for key, vaiue in dictionary_2.items() if letter in vaiue] 
result_2 = [key for letter in i for key, vaiue in dictionary_1.items() if letter in vaiue]

print(sum(result_1 + result_2))






