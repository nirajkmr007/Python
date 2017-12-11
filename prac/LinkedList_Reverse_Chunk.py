'''
Created on Dec 9, 2017

@author: Niraj.Kumar
'''
from prac.LinkedList_Reverse import prev

'''reverse a link list in chunks, example chunk size(k) = 3 
input  : 1 2 3 4 5 6 7 8 
output : 3 2 1 6 5 4 8 7
'''

from model.LinkedList import SingleLinkedList

ll = SingleLinkedList()

for i in range(17,0,-1):
    ll.add(i)

def printLL(head):
    temp = head
    while(temp != None):
        print(temp.getData())
        temp =temp.getNext()
        
printLL(ll.head)

'First Way'

def reverseLL(head):
    prev = None
    current = head
    next = None
    
    while(current.getNext()!= None):
        next = current.getNext()
        current.setNext(prev)
        prev = current
        current = next
    current.setNext(prev)
    return current,head
    
k =3

current = ll.head
i=1
newHead = None
nextBlock = None
oldTail = None
oldHead = ll.head
while(current.getNext() != None):
    if(i % k == 0):
        nextBlock = current.getNext()
        current.setNext(None)
        head,tail = reverseLL(oldHead)
        oldHead = nextBlock
        if(newHead == None):
            newHead = head
        else:
            oldTail.setNext(head)
        oldTail = tail
        current = nextBlock 
    else:
        current = current.getNext()       
    i += 1
head,tail = reverseLL(oldHead)
oldTail.setNext(head)

printLL(newHead)




'Second Way'

newHead = None
k = 4
current = ll.head
prev = None
v1 = ll.head
v2 =None

i = 0

while(current.getNext() != None):
    i += 1
    temp = current.getNext()
    current.setNext(prev)
    prev = current
    current = temp
    if(i % k == 0):
        #temp = current.getNext()
        if(newHead == None):
            newHead = prev
        else:
            v1.setNext(prev) 
            v1 = v2
        v2 = current
            
   
    
current.setNext(prev)
v1.setNext(current)
v2.setNext(None)      
    
printLL(newHead)

