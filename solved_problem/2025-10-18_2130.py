# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #Method 1: Cheat with Array: Time Complexity O(n) Space Complexity 0(n)
        #1) Tranverse
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        #2) Find max
        max_sum = 0
        for i in range(len(arr)//2):
            if arr[i] + arr[len(arr)-1-i] > max_sum:
                max_sum = arr[i] + arr[len(arr)-1-i]
        return max_sum

        #Method 2: Reverse linked list: Time Complexity O(n) Space Complexity 0(1)
        head1 = head2 = head
        #1) Find midpoint
        l = 0
        while head1:
            head1 = head1.next
            l+=1
        m = l//2

        #2) Reverse second half
        for i in range(m):
            head2 = head2.next

        curr = head2 
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
            
        #3) Find max
        first_half = head 
        second_half = prev # Just for clarity
        
        res = 0
        for i in range(m):
            res = max(first_half.val + second_half.val, res)
            first_half = first_half.next
            second_half = second_half.next
        return res 