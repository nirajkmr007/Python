'''
Created on Nov 23, 2017

@author: Niraj.Kumar
'''

left=[1,3,6,None,None,None,None,None]
right=[2,4,5,7,8]
leftlen = len(left) - len(right)
#a=[0,0,0,0,0,0,0,0]
i=0 
j=0
k=0
while(i<leftlen and j<len(right)):
    if(left[i]>right[j]):
        temp = right[j]
        right[j]=left[i]
        left[i]=temp
    i+=1
        
'''while(i<len(left)):
    a[k]=left[i]
    i+=1
    k+=1'''
while(i<len(left)and j<len(right)):
    left[i]=right[j]
    i+=1
    j+=1

print(left)