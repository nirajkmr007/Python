'''
Created on Dec 9, 2017

@author: Niraj.Kumar
'''


from model.LinkedList import SingleLinkedList

ll = SingleLinkedList()

for i in range(1,10):
    ll.add(i)

temp = ll.head
while(temp != None):
    print(temp.getData())
    temp =temp.getNext()
    

prev = None
current = ll.head


while(current.getNext()!= None):
    next = current.getNext()
    current.setNext(prev)
    prev = current
    current = next
current.setNext(prev)

temp = current
while(temp != None):
    print(temp.getData())
    temp =temp.getNext()
    