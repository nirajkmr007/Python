'''
Created on Nov 25, 2017

@author: Niraj.Kumar
'''

'in a given matrix if any cell has 0 make all row and column value of that cell to 0'
'''input  1 2 1 2 
          2 4 1 4
          1 8 0 3
          2 3 4 5
      
output    1 2 0 2 
          2 4 0 4
          0 0 0 0
          2 3 0 5 '''
          
a = [[1,2,1,2],[2,4,1,4],[1,8,0,3],[2,3,4,5]]

for i in a:
    for j,l in enumerate(i):
        if l==0:
            a[j]=[0]*len(a[j])
            for k,s in enumerate(a):
                a[k][j] = 0
            #pass
for i in a:
    print(i)