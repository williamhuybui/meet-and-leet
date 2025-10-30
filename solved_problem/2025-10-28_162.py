class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            m=(l+r)//2
            if m+1 < len(nums):
                if nums[m]>=nums[m+1]:
                    r = m 
                else:
                    l=m+1
        return l

        

