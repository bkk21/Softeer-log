import sys

tmp = input()
tmplist = tmp.split()
a = int(tmplist[0])
b = int(tmplist[1])
d = int(tmplist[2])

time = 0 
main = 0

if a >= d: #갈 때와 거리가 같을 때
    if b >= d: #올 수 있는 시간이 거리보다 크거나 같을 때
        time += a
        time += d

    elif b < d: #올 수 있는 시간이 거리보다 작을 때
        main = d
        while main > 0:
            time += a
            if b < main:
                time += b
                main -= b
            else:
                time += main
                main -= main

elif a < d:
    if b >= d:
        main = d
        time += a
        while main > 0:
            time += b
            main -= a
            if a < main:  
                time += a
            else:
                time += main
        time += d
    
    if b < d:
        main = d
        time += a
        time += b
        main -= a
        while main > 0:
            if a < main:  
                time += a
                time += b
                main -= a
            else:
                time += main
                main -= main
        
        main = d
        time += b
        time += a
        main -= b
        while main > 0:
            if b < main:  
                time += b
                time += a
                main -= b
            else:
                time += main
                main -= main
        
print(time)