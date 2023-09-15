"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = {}
        n = 0
        og_head = head
        while og_head:
            new_nodes[og_head] = Node(og_head.val)
            og_head = og_head.next
            n += 1
        
        if n == 0:
            return None
        
        curr = head
        while curr:
            new_nodes[curr].next = new_nodes.get(curr.next)
            new_nodes[curr].random = new_nodes.get(curr.random)
            curr = curr.next

        return new_nodes[head]

        