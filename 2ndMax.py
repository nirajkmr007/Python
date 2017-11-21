'''
Created on Oct 29, 2017

@author: Niraj.Kumar
'''

l = [13,4,2,11,5,6,9,0]

currentMax= l[0]
scndMax =-9999999

for index,i in enumerate(l):
    if i > scndMax and index > 0:
        scndMax = i
    if i > currentMax and index > 0:
        scndMax = currentMax
        currentMax = i

print(currentMax,scndMax)