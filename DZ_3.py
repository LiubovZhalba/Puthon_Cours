# Задача 16: Подсчитать сколько раз встречается число 
#print(len(set(list_dialects)))

n = int(input())
lst = []
for i in range(n):
    
    num = int(input())
    lst.append(num)

    count = 0
       
    if lst[i] == num:
        count = count + 1
print(count)