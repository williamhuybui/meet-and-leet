# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
#Method 1: Cheat method 
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        head1 = head2 = head
        #Get all values
        while head1:
            nums.append(head1.val)
            head1 = head1.next
        #Alternate order
        odd_num, even_num = [], []
        for i in range(len(nums)):
            if i%2 == 0:
                even_num.append(nums[i])
            else: odd_num.append(nums[i])
        nums = even_num + odd_num
        #Reassign to the LL
        for i in range(len(nums)):
            head2.val = nums[i]
            head2 = head2.next
        return head

# Method 2
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        #Method 2:
        odd_head = head #Even index head
        even_head = even_head_2 = head.next #Odd index head

        while even_head_2 and even_head_2.next:
            odd_head.next = odd_head.next.next
            odd_head = odd_head.next
            even_head_2.next = even_head_2.next.next
            even_head_2 = even_head_2.next
            
        odd_head.next = even_head
        return head