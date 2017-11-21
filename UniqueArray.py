'''
Created on Nov 9, 2017

@author: Niraj.Kumar
'''

arr = [6,7,8,3,4,0,0]
mx = arr[0]
for a in arr:
    if a > mx:
        mx=a
         
lst = [0]*(mx+1)

for a in arr:
    if lst[a] == 1:
        print("not unique")
    else:
        lst[a] = 1
    