#틀림 다시 풀 것
import sys

list_a = []
min = 4

for i in range(3):
    a, b, c = input().split()
    list_a.append(a)
    list_a.append(b)
    list_a.append(c)

for i in range(6):
    if i == 0:
        tmp1 = int(list_a[i])
        tmp2 = int(list_a[i+1])
        tmp3 = int(list_a[i+2])
        
        if tmp1 == tmp2 and tmp2 == tmp3:
            min = 0
            
        elif tmp1 == tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
                
        elif tmp1 != tmp2 and tmp2 == tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
                
        elif tmp1 == tmp3 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
        
        elif tmp1 != tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
            elif min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
            elif min > int(abs(tmp3 - tmp1)):
                min = int(abs(tmp3 - tmp1))
        
        tmp1 = int(list_a[i])
        tmp2 = int(list_a[i+1])
        tmp3 = int(list_a[i+2])
        
        if tmp1 == tmp2 and tmp2 == tmp3:
            min = 0
            
        elif tmp1 == tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
                
        elif tmp1 != tmp2 and tmp2 == tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
                
        elif tmp1 == tmp3 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
        
        elif tmp1 != tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
            elif min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
            elif min > int(abs(tmp3 - tmp1)):
                min = int(abs(tmp3 - tmp1))
        
    if i == 1 or i == 2:
        tmp1 = int(list_a[i])
        tmp2 = int(list_a[i+3])
        tmp3 = int(list_a[i+6])
        if tmp1 == tmp2 and tmp2 == tmp3:
            min = 0
            
        elif tmp1 == tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
                
        elif tmp1 != tmp2 and tmp2 == tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
                
        elif tmp1 == tmp3 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
        
        elif tmp1 != tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
            elif min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
            elif min > int(abs(tmp3 - tmp1)):
                min = int(abs(tmp3 - tmp1))
        
    if i == 3 or i == 6:
        tmp1 = int(list_a[i])
        tmp2 = int(list_a[i+1])
        tmp3 = int(list_a[i+2])
        if tmp1 == tmp2 and tmp2 == tmp3:
            min = 0
            
        elif tmp1 == tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
                
        elif tmp1 != tmp2 and tmp2 == tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
                
        elif tmp1 == tmp3 and tmp2 != tmp3:
            if min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
        
        elif tmp1 != tmp2 and tmp2 != tmp3:
            if min > int(abs(tmp1 - tmp2)):
                min = int(abs(tmp1 - tmp2))
            elif min > int(abs(tmp2 - tmp3)):
                min = int(abs(tmp2 - tmp3))
            elif min > int(abs(tmp3 - tmp1)):
                min = int(abs(tmp3 - tmp1))

print(min)