'''
Created on Nov 25, 2017

@author: Niraj.Kumar
'''

'in a given matrix if any cell has 0 make all row and column value of that cell to 0'
'''input  1 2 1 2 
          2 4 1 4
          1 8 0 3
          2 3 4 5
          0 3 4 5
      
output    0 2 0 2 
          0 4 0 4
          0 0 0 0
          0 3 0 5 
          0 0 0 0
          '''
          
a = [[0,2,1,0],[2,4,1,4],[1,8,9,3],[2,3,4,5],[0,3,4,0]]
row = [0]*len(a)
col = [0]*len(a[0])
'first way time complexity O(m*n) space complexity O(m*n)'
for i in range(len(a)):
    for j in range(len(a[0])):
        #print(i,j)
        if(a[i][j] == 0):
            row[i] = 1
            col[j] = 1
            #pass
for i in range(len(a)):
    for j in range(len(a[0])):
        if(row[i] == 1 or col[j] == 1):
            a[i][j]=0
            
for i in a:
    print(i)

print("")
'Second way time complexity O(m*n) space complexity O(1)'
a = [[9,2,1,0],[2,4,1,4],[1,8,9,3],[2,3,4,5],[0,3,4,9]]
row = False
col = False

for i in range(len(a)):
    for j in range(len(a[0])):
        #print(i,j)
        if(a[i][j] == 0):
            if(i == 0):
                row = True
            if(j == 0):
                col = True
            a[i][0] = 0
            a[0][j] = 0
            
for i in range(1,len(a)):
    for j in range(1,len(a[0])):
        #print(i,j)
        if(a[i][0] == 0 or a[0][j] == 0):
            a[i][j]=0

if(row == True):
    for i in range(len(a[0])):
        a[0][i]=0
if(col == True):
    for i in range(len(a)):
        a[i][0]=0
        
for i in a:
    print(i)