class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        #Time O(n), Space O(1)
        left, right = 0, 0
        curr = 0 
        res = 0
        while right < len(nums):
            if nums[right] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res