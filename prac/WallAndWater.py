'''
Created on Nov 24, 2017

@author: Niraj.Kumar
'''


'''in given array height of walls are there which are build next to each other with no gap in between, 
width of every wall is 1 unit. you have to find two walls by keeping them if you will break all others walls
it will keep maximum possible volume of water. '''

a = [3,3,1,5,3,1]

mx = 0

'brute force approach'
for i,item1 in enumerate(a):
    for j,item2 in enumerate(a):
        temp = (j-i-1)*min(item1,item2)
        if j>i and temp > mx:
            mx = temp
            #print(i,j)
print(mx)