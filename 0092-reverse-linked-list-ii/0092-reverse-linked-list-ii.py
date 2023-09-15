# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        index = 1
        dummy = ListNode(0, head)
        prev = dummy

        while index < left:
            prev = prev.next
            index += 1
        
        curr = prev.next

        while index < right:
            next_node = curr.next
            
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
            index += 1

        return dummy.next