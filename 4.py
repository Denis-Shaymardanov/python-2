'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. 
Позиции вводятся через пробел одной строкой.
n = 3
[-3, -2, -1, 0, 1, 2, 3]
'0 2 4'
res -> 3'''
n=int(input("Введите N "))
array = []
index = 0
for i in range(-n,n+1):
    array.append(i)
indexes=input("Введите индексы через пробел ").split()
result = 1
for i in (indexes):
    result*=array[int(i)]
print(array)
print(result)
