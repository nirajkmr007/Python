'''
Created on Nov 27, 2017

@author: Niraj.Kumar
'''

'in given array find the first element, left of which all are small and right of all are bigger'

'''input :     5 1 4 3 6 8 7 11 12
output : 6'''

'time complexity O(n)'

a = [5, 1, 4, 3, 2, 1,10]

current = a[0]

for i in range(1,len(a)):
    if(a[i]>=current):
        pass
    else:
        if(i<len(a)-1):
            if(a[i+1] > current):
                current = a[i+1]
        else:
            current = -1
print(current)
