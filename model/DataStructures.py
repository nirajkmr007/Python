'''
Created on Dec 5, 2017

@author: Niraj.Kumar
'''

class Stack(object):
    '''
    DataStructure : Stack implementation
    '''

    slist =[]
    top = -1
    max = None

    def __init__(self, size):
        '''
        Constructor
        '''
        self.max= size
    
    def push(self,item):
        if(self.top<self.max):
            self.slist.append(item)
            self.top+=1
            return True
        else:
            print("Stack is full")
            return False
    
    def pop(self):
        if(self.top>-1):
            poped_item = self.slist[self.top]
            self.top-=1
            return poped_item
        else:
            print("Stack is Empty")
        
    def get_top(self):
        return self.top
    
    def is_empty(self):
        return self.slist == []
    
    'end of stack'
    
    class Queue(object):
        '''
        DataStructure : Queue implementation
        '''
        qlist = []
        rear = -1
        front = -1
        max = None
        def __init__(self, size):
            self.max=size
        def pop_first(self):
            if(self.front > -1):
                poped_item = self.front
                self.front += 1
                return poped_item
            else:
                print("Queue is empty")
        def pop_last(self):
            if(self.rear >self.front):
                print("Queue is empty")
            poped_item = self.front
            self.rear += 1
            return poped_item
            
        def insert(self, item):
            if(self.front == -1):
                self.front =0
            if(self.rear < self.max):
                self.qlist.append(item)
                self.rear +=1
            else:
                print("Queue is full")