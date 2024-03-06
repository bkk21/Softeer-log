import sys

num = int(input())

for n in range(num):
    a = int(input())
    a1 = a // 5
    a2 = a % 5

    i = 0 
    p_a = ""
    for i in range(a1):
        p_a += "++++ "

    for i in range(a2):
        p_a += "|"

    print(p_a)