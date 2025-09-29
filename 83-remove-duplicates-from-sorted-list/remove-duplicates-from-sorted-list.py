# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                # If current node's value is equal to the next node's value,
                # skip the next node (which is a duplicate)
                current.next = current.next.next
            else:
                # If they are different, move to the next node
                current = current.next
        
        return head