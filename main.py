# Делаем срезы
# s = str('qwerty')
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])
# print(len(s))

# Колличество слов
# s = input()
# k = s.count(' ')
# print(k+1)

# Две пполовинки
# s = 'qwertyuio'
# a = s[:round(len(s)/2)]
# b = s[len(s)//2:]
# print(a, b)

# первое и последние вхождение
# s = 'float_file'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))

# Удаление фрагмента
# s = input()
# s = s[:s.find('h')] + s[s.rfind('h') + 1:]
# print(s)

# Замена подстроки
# print(input().replace('1', 'one'))

# Удаление символа
# print(input().replace('@', ' '))

# Замена внутри фрагмента
# s = input()
# a = s[:s.find('h') + 1]
# b = s[s.find('h') + 1:s.rfind('h')]
# c = s[s.rfind('h'):]
# s = a + b.replace('h', 'H') + c
# print(s)

# Миниум из двух чисел
# a = int(input())
# b = int(input())
# if a>b:
#  print(b)
# else:
#  print(a)

# Знак числа
# x = int(input())
# if x>0:
#     print('sign(x)=1')
# elif x<0:
#     print('sign(x)-1')
# else:
#     print('sign(x)=0')

# Шахматная доска
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if 1<=x1<=8 and 1<=x2<=8 and 1<=y1<=8 and 1<=y2<=8:
#     if (x1+y1)%2 == (x2+y2)%2:
#     print('yes')
# else:
#     print('no')
# else:
#     print('Такой клеточки нет')

# Високосный год
# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('yes')
# else:
#     print('no')

# Сколько совпадает чисел
# a = int(input())
# b = int(input())
# s = int(input())
# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)

# Ход ладьи
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print('yes')
# else:
#     print('no')

# Шоколадка
# n = int(input())
# m = int(input())
# k = int(input())
# if (k%n==0 or k%0==m) and k<n*m:
#     print('yes')
# else:
#     print('no')


























