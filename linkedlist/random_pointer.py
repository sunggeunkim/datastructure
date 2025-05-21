from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList_ON(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        map_nodes = {}
        pointer = head
        while pointer:
            new_node = Node(pointer.val)
            map_nodes[pointer] = new_node
            pointer = pointer.next
        pointer = head
        while pointer:
            new_node = map_nodes[pointer]
            new_node.next = map_nodes[pointer.next] if pointer.next else None
            new_node.random = map_nodes[pointer.random] if pointer.random else None
            pointer = pointer.next
        return map_nodes[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        current = head
        while current:
            copy_node = Node(current.val, next=current.next)
            next_node = current.next
            current.next = copy_node
            current = next_node

        current = head
        new_head = current.next

        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next

        current = head
        while current:
            next_current_node = current.next.next
            current.next.next = current.next.next.next if next_current_node else None
            current.next = next_current_node.next if next_current_node else None
            current = next_current_node

        return new_head

        # current = head
        # while current:
        #     current.random.next = current.next.random if current.next else None
        #     current = current.next
        # newhead = head.random
        # current = newhead
        # while current:
        #     current.random = current.random.random if current.random else None
        #     current = current.next
        # return newheadv

s = Solution()
x = [Node(7), Node(13), Node(11)]
x[0].next = x[1]
x[1].next = x[2]
x[2].next = None
x[0].random = None
x[1].random = x[0]
x[2].random = x[1]
newx = s.copyRandomList(x[0])
print(newx)