'''
Created on Nov 23, 2017

@author: Niraj.Kumar
'''

left=[2,4,5,7,8,None,None,None]
right=[1,3,6]

totallen = len(left)
rightlen = len(right)
leftlen = totallen - rightlen

#a=[0,0,0,0,0,0,0,0]

while(leftlen >0 and rightlen>0):
    if(left[leftlen-1]>right[rightlen-1]):
        left[totallen-1]=left[leftlen-1]
        left[leftlen-1] =None
        leftlen-=1
    else:
        left[totallen-1]=right[rightlen-1]
        rightlen-=1
    totallen-=1
while(rightlen>0 and totallen>0):
    left[totallen-1]=right[rightlen-1]
    rightlen-=1      
    totallen-=1

print(left)