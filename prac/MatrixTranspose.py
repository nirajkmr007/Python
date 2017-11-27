'''
Created on Nov 27, 2017

@author: Niraj.Kumar
'''

'transpose the given matrix'
'''input  1 2 3 4 
          1 2 3 4
          1 2 3 4
          1 2 3 4
      
output    1 1 1 1 
          2 2 2 2
          3 3 3 3
          4 4 4 4 '''

       
a = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
c = [[0]*len(a) for _ in range(len(a[0]))]
#c = copy.deepcopy(a) # assigning a variable to other is just a reference to original 

for i, rows in enumerate(a):
    for j,item in enumerate(rows):
        #print(a[j][i])
        c[j][i] = item

for i in c:
    print(i)