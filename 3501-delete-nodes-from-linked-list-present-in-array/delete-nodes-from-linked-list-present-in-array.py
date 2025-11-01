# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        to_delete = set(nums)   # convert nums to set for O(1) lookup
        dummy = ListNode(0)     # create a dummy node
        dummy.next = head
        prev, curr = dummy, head

        # traverse the linked list
        while curr:
            if curr.val in to_delete:
                prev.next = curr.next  # skip the node
            else:
                prev = curr             # move prev forward only if not deleted
            curr = curr.next            # move current forward

        return dummy.next 