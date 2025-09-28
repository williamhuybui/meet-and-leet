from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Method 1: O(n) time, O(n) space
        h_map = {} 
        for val in arr:
            if val not in h_map: #Set look up O(1)
                h_map[val] = 1
            else:
                h_map[val] += 1
        occurrences = h_map.values()
        return len(occurrences) == len(set(occurrences))

        # #Method 2: O(n) time, O(n) space
        # occurrences = Counter(arr).values()
        # return len(occurrences) == len(set(occurrences))