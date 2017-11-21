'''
Created on Oct 27, 2017

@author: Niraj.Kumar
'''


class TOH(object):
    '''
    Tower of hanoi finds minimun steps 
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def towerOfHanoi(self,num):
        if(num == 1):
            return 1
        else:
            return 2*self.towerOfHanoi(num-1)+1


toh = TOH().towerOfHanoi(5)
print(toh)          