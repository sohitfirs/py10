import random

def pl(l):
    for i in l:
        print(i)

x = int(input('input x: '))
y = int(input('input y: '))

l1 = [[int(random.randint(-10, 10)) for j in range(y)] for i in range(x)]

l2 = [[int(random.randint(-10, 10)) for j in range(y)] for i in range(x)]

l3 = [[[] for j in range(y)] for i in range(x)]

print('\nmatrix #1')
pl(l1)

print('\nmatrix #2')
pl(l2)

for i in range(x):
    for j in range(y):
        l3[i][j] = l2[i][j] + l1[i][j]

print('\nmatrix #3')
pl(l3)

input()