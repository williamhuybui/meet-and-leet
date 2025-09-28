class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        #Method 1: Time: O(m*n). Space: O(m+n)
        ans = [[], []]
        for num in nums1: #(O(n))
            if (num not in ans[0]) and (num not in nums2): #(O(m)): List look up
                ans[0].append(num)
        for num in nums2:#(O(m))
            if (num not in ans[1]) and (num not in nums1):#(O(n)) : List look up 
                ans[1].append(num)
        return ans

        # # Method 2: Time: O(m+n). Space: O(m+n)
        # #Set difference: O(n) 
        # # Set look up: O(1)
        # return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]