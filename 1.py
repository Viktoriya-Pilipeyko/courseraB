""" a = int(input())
b = int(input())
c = int(input())
d = int(input())

for l in range(c, d+1):
    print('\t',l, end = '')
print('')
for i in range(a,(b+1)):
    print(i, end='')
    for j in range(c, d+1):
        print('\t', i * j, end = '')
    print('') """

""" a, b = (int(i) for i in input().split())
s = 0
c = 0

for i in range(a, b+1):
    if i % 3 == 0:
        s += i
        c += 1
print(s / c) """

""" a = input()
l = 'letter'
r = ''
for i in a:
    if i != l:
        r += i + str(a.count(i))
    l = i
print(r) """

""" s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t += s + str(c)
else:
    for i in range(l):
        if s[i] == s[i+1]:
            c += 1
        elif s[i]!=s[i+1]:
            t += s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t += s[j]+str(c)
            c = 1
print(t) """

""" import webbrowser

webbrowser.open('https://jira.sberbank.ru/browse/LINEUP-26088', new = 2) """

""" l = [int(i) for i in input().split()]

for i in range(len(l)):
    if len(l) == 1:
        print(l[i])
    elif i == len(l) - 1:
        print(l[i-1] + l[0], end = ' ')
    else:
        print(l[i-1] + l[i+1], end = ' ') """

""" a = input().split()
a.sort()
l = []
for i in a:
    if a.count(i) == 1:
        continue
    elif a.count(i) > 1 and i not in l:
        print(i, end = ' ')
        l.append(i) """

#выводить сумму квадратов чисел, если сумма чисел равна 0
""" a = int(input())
s = a * a
while a != 0:
    i = int(input())
    s += i * i
    a += i

print(s) """

#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). 
# На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. 
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
""" a = int(input())
l = []

for i in range(1,a + 1):
    for j in range(1,i+1):
        if len(l) < a:
            l.append(i)
            print(i, end = ' ') """

#Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, 
# которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
#Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
#Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
""" lst = input().split()
x = int(input())
r = 0
for i, e in enumerate(lst):
    if int(e) == x:
        print(i, end = ' ')
        r = i
if r == 0:
    print('Отсутствует') """

#v2
""" lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
	if x == lst[i]:
		print(i, end=' ')

if x not in lst:
    print('Отсутствует') """


#Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. 
# После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).
#Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен 
#сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
#В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
""" l = input()
lst = []
while l != 'end':
    lst.append([int(j) for j in l.split()])
    l = input()

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if j == len(lst[i]) - 1 and i == len(lst)-1:
            print(lst[i-1][j] + lst[0][j] + lst[i][j-1] + lst[i][0], end = ' ')
        elif j == len(lst[i]) - 1:
            print(lst[i-1][j] + lst[i+1][j] + lst[i][j-1] + lst[i][0], end = ' ')
        elif i == len(lst)-1:
            print(lst[i-1][j] + lst[0][j] + lst[i][j-1] + lst[i][j+1], end = ' ')
        else:
            print(lst[i-1][j] + lst[i+1][j] + lst[i][j-1] + lst[i][j+1], end = ' ')
    print() """


#Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2n 2
#по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):

def spiral(n):
    dx,dy = 1,0           
    x,y = 0,0              
    myarray = [[None]* n for j in range(n)]
    for i in range(1,n**2+1):
        myarray[x][y] = i
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
            x,y = nx,ny
        else:
            dx,dy = -dy,dx
            x,y = x+dx, y+dy
    return myarray
 
def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print (myarray[x][y],end=' ')
        print()

n = int(input())
printspiral(spiral(n))
