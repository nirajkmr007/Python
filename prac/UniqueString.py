'''
Created on Nov 25, 2017

@author: Niraj.Kumar
'''

'find string contain unique elements or not'

st = "abcadf5876%"

'Time complexity -> O(n) : space complexity -> O(1) by using array DS'
d=[0]*256
flag = True

for a in st:
    if(d[ord(a)]==0):
        d[ord(a)]=1
    else:
        flag = False
        break

if(flag):
    print("yes")
else:
    print("no")
    
'Time complexity -> O(n) : space complexity -> O(1) without using any data structure'
flag = True
f = 0
#print(bin(3))
for a in st:
    i = ord(a)
    s = 1<<i
    #print(bin(s)) 
    if s & f == 0:
        f = f | s
    else:
        flag = False
        break
if(flag):
    print("yes")
else:
    print("no")