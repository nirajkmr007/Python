'''
Created on Oct 24, 2017

@author: Niraj.Kumar
'''

lst = [7,6,6,3,9,3,5,1]
k = 12
my_set = set()

for i in lst:
    for j in lst:
        if(i != j and i + j == k):
            my_set.add(i)
            my_set.add(j)

print(int(len(my_set)/2))