'''
Created on Dec 10, 2017

@author: Niraj.Kumar
'''

''' find the kth element from last in given linked list
'''


from model.LinkedList import SingleLinkedList

ll = SingleLinkedList()

for i in range(13,0,-1):
    ll.add(i)

def printLL(head):
    temp = head
    while(temp != None):
        print(temp.getData())
        temp =temp.getNext()
        
printLL(ll.head)

k = 3
i = 1
current = ll.head
kth = current
while(current.getNext() != None):
    if(i >= k):
        kth = kth.getNext()
        
    current = current.getNext()
    i+=1
print(kth.getData())