import sys

num = int(input())

v = list(range(num))

a = input()
v = a.split()

i = 0
count = 0
for i in range(num):
    if i != num-1:
        op = int(v[i+1]) - int(v[i])
        if i == 0:
            tmp = op
            count += 1
        else:
            if op == tmp:
                count += 1
            elif op < tmp:
                count = 1
                tmp = op

print(count)