import re
from re import search

#1
#print(len(set(input().split())))

#2
#print(len(set(input().split()) & set(input().split())))

#3
#print(sorted(set(input().split()) & set(input().split()), key=float))

#4
#a = input().split()
#seen = set()
#print('\n'.join(f'{x}: NO' if x not in seen and not seen.add(x) else f'{x}: YES' for x in a))

#5
# b = ''
# for i in range(0, int(input())):
#     b += input()
# print(set(re.sub(r'\.|,|;|:|\s', ' ', b).lower().split()))

#6
# a = {}
# c = ''
# for i in range(0, int(input())):
#     c = input()
#     a[c] = a[c] + 1 if (c in a.keys()) else 1
#
# print(sum(x for x in a.values() if x!= 1))

#7
# a = {}
# for i in input().split():
#     a[i] = a[i] + 1 if (i in a.keys()) else 1
# print(a)

#8
# a={}
# for i in range(0, int(input('Введите количество пар: '))):
#     pair = input(f'{i+1} пара: ').lower().split()
#     a[pair[0]] = pair[1]
#     a[pair[1]] = pair[0]
# search_word = input('Введите слово для поиска: ').lower()
# print(a[search_word]) if search_word in a else print('Такого слова нет.')

#9
# a={}
# for i in range(0, int(input())):
#     pair = input().split()
#     if pair[0] not in a:
#         a[pair[0]] = int(pair[1])
#     else:
#         a[pair[0]] += int(pair[1])
# [print(f"{key}: {value}") for key, value in dict(sorted(a.items())).items()]

#10
a={}
for i in range(0, int(input())):
    pair = input().lower().split(' ', 1)
    a[pair[0]] = pair[1].replace('x', 'e')
for i in range(0, int(input())):
    command = input().lower().split()
    print('OK') if (command[0][0] in a[command[1]]) else print('access denied')