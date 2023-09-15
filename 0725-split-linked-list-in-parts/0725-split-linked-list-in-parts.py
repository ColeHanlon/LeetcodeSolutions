# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0
        og_head = head
        while head:
            head = head.next
            count += 1

        bucket_base = int(count / k)
        bucket_remainder = int(count % k)
        bucket_sizes = [0] * k

        for i in range(0, k):
            bucket_sizes[i] = bucket_base
            
        final_buckets = [0] * k
        index = 0
        while bucket_remainder > 0:
            if index == k:
                index = 0
            
            bucket_sizes[index] += 1
            index += 1
            bucket_remainder -= 1
            
        output = [None] * k
        curr = og_head
        prev = None
        for i in range(0, k):
            item_count = bucket_sizes[i]
            
            while item_count > 0:
                if item_count == bucket_sizes[i]:
                    output[i] = curr
                else:
                    prev.next = curr

                prev = curr
                curr = curr.next
                item_count -= 1

            if prev:
                prev.next = None

        return output


