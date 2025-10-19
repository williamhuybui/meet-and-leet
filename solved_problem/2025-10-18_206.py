from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Method 2:
        current_head = head
        prev_head = None
        while current_head:
            temp = current_head.next #Save for current for the next iteration
            current_head.next = prev_head #Change direction
            prev_head = current_head #Prepare for next interartion for prev
            current_head = temp #Prepare for next interartion for curr
        return prev_head