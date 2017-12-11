'''
Created on Dec 10, 2017

@author: Niraj.Kumar
'''

''' find the merging element in two given linked list

1->2->3->4->5->6
        /\  
         | 
1->2->3--

output : 4 is merging element here

'''

from model.LinkedList import SingleLinkedList

ll = SingleLinkedList()

for i in range(13,0,-1):
    ll.add(i)