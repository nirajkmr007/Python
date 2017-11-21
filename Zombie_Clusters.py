'''
Created on Oct 24, 2017

@author: Niraj.Kumar
'''

k =4
mat = ['1100' '1110', '0110', '0001']
relations = set()

for i in len(mat):
    for j in len(mat):
        if(i != j and mat[i][j] == 1):
            relations.add(i)
            relations.add(j)
#cluster = 