# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:56:26 2022

@author: Sally
"""

# range(6) => [0,1,2,3,4,5]
# range(1,6) => [0,1,2,3,4,5]
# range(2,6) => [2,3,4,5]

'''
for a in range(1,6):    # [1,2,3,4,5]
    for x in range(a):  # 迴圈的次數由a來決定
        print(x,end='')
    print()

print()
'''

# a = 1
#   for x in range(1):[0]
#       print(x)

# a = 2
#   for x in range(2):[0,1]
#       print(x)

# a = 3
#   for x in range(3):[0,1,2]
#       print(x)
    
# 第一個作業
for b in range(1,6):
    for y in range(1,b+1):
        print(b,end='')  
    print()
    
print()
 
# 第二個作業
for c in range(5,0,-1):
    for z in range(0,c):
        print(c,end='')
    print()
    
print()
    
# 第三個作業
for d in range(9,0,-2):
    for z in range(0,d):
        print(d,end='')
    print()
    
print()

# 第四個作業
for pn in range(2,11):
    if (pn == 2 or pn == 3 or pn == 5 or pn == 7):
        print(pn)
for pn in range(11,101):
    if (pn %1 == 0 and pn % pn == 0 and pn %2 != 0 and pn %3 != 0 and pn %5 != 0 and pn %7 !=0):
        print(pn)
# 第四個作業        
for pn in range(2,101):
    if (pn == 2 or pn == 3 or pn == 5 or pn == 7):
        print(pn)
    elif (pn %1 == 0 and pn % pn == 0 and pn %2 != 0 and pn %3 != 0 and pn %5 != 0 and pn %7 !=0):
        print(pn)



"""
第一個作業
1
22
333
4444
55555

第二個作業
55555
4444
333
22
1

第三個作業
999999999
7777777
55555
333
1

第四個作業
求質數： 可以被 1 及自己整除的數稱為質數
請輸入1~100之間的質數有哪些
"""