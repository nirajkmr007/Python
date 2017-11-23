'''
Created on Nov 21, 2017

@author: Niraj.Kumar
'''


a = [4,8,9,2,1,11,3,12,7]

def mergeSort(a):
    l = len(a)
    if(l==1):
        return a
    else:
        mid = l//2
        left=a[:mid]
        right=a[mid:]
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                a[k]=left[i]
                i+=1
            else:
                a[k]=right[j]
                j+=1
            k+=1
        while(i<len(left)):
            a[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            a[k]=right[j]
            j+=1
            k+=1
        mergeSort(left)
        mergeSort(right)
    print(a)
    
mergeSort(a)
    