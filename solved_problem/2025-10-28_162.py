class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        #i = 0
        while lo < hi:
            #print('loop',i,' and ', nums[lo], nums[hi])
            mid = (lo + hi) // 2
            #print(nums[mid], nums[mid + 1])
            if nums[mid] < nums[mid + 1]: #increasing array on right
                lo = mid + 1          # peak is on the right
            else:  #decreasing array on right so peak must be on left side, mid can be peak
                hi = mid              # peak is on the left (including mid)
            #i += 1    
        return lo                     # lo == hi, a peak index