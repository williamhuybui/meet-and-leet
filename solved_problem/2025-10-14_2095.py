# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Find the lenghth of the LL
        count = 0
        head1 = head2 = head
        while head1:
            count += 1
            head1 = head1.next

        #Find the mid point of LL
        m = count // 2

        #Edge cases
        if count == 1:
            return None
        if count == 2:
            head.next = None 
            return head

        #Tranverse a node before the middle node
        while m-1 != 0: #Before
            head2 = head2.next
            m-=1
        #Skip the middle node
        head2.next = head2.next.next
        return head