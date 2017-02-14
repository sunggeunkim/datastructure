# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:48:17 2017

@author: Kim
"""

            
from question1 import question1
from question2 import question2        
from question3 import Graph, question3        
from question4 import question4
from question5 import question5, Node

#test question1
print question1("udacity", "adu")
print question1("udacity", "yti")
print question1("udacity", "dci")
print question1("udacity", "a")
print question1("udacity", "")
print question1("udacity", "aic")
print question1("udacity", "tyaucdi")

#test question2
print question2('abcbcbad')
print question2('')
print question2('c')
print question2('bcb')

#test question3
graph = Graph()
graph.insert_edge(2, 'A', 'B')
graph.insert_edge(5, 'B', 'C')
graph.insert_edge(4, 'B', 'D')
graph.insert_edge(6, 'C', 'D')
graph.insert_edge(3, 'A', 'C')
adj_list = graph.get_adjacency_list()
print question3(adj_list)

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

print question4([[0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          2)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print question5(head, 3)
