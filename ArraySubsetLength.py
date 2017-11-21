'''
Created on Oct 30, 2017

@author: Niraj.Kumar
'''

l = [2,2,-1,-5,4,1,1,-1]

lsize=len(l)
i=0
j=lsize
sumOfList = sum(l)

while(sumOfList!=0 and len(l[i:j])!=1):
    if(j == lsize):
        j-=i+1
        i=0
    else:
        i+=1
        j+=1
    sumOfList = sum(l[i:j])
    
print("Max sublist size : {} val {}".format(len(l[i:j]), l[i:j]))
    
    
    