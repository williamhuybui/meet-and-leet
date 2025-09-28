class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitudes = 0
        max_altitudes = altitudes
        for i in range(len(gain)):
            altitudes = altitudes+gain[i]
            max_altitudes = max(altitudes,max_altitudes)
        return max_altitudes