from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Method 1: Nested for loop O(N^2)
        # ans = []
        # for i in range(len(temperatures)-1):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans.append(j-i)
        #             break
        #         elif j == len(temperatures) - 1:
        #             ans.append(0)
        # ans.append(0)
        # return ans

        # Method 2: Stack O(N)
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                last = stack.pop()
                ans[last[0]] = i-last[0]
            stack.append((i,temperatures[i]))
        return ans

# temp = [73,74,75,71,69,72]
# ans  = [1, 1, 0, 2, 1, 0 ]
# stack= [(0,73)] see (0,73)
# stack= [(0,73)] see (1,74) since 74 > 73 update ans[0] = 1 - 0, pop stack, update stack 
# stack= [(1,74)] see (2,75) since 75 > 74 update ans[1] = 2 - 1, pop stack, update stack 
# stack= [(2,75)] see (3,71) since 71 < 75 update stack 
# stack= [(2,75), (3,71)] see (4,69) since 69 < 71 update stack 
# stack= [(2,75), (3,71), (4,69)] see (5,72) since 72 > 69 update ans[4] = 5 - 4, pop stack, repeat 
# stack= [(2,75), (3,71)] see (5,72) since 72 > 71 update ans[3] = 5 - 3, pop stack, repeat 
# stack= [(2,75)] see (5,72) since 75 > 72 update stack 
# stack= [(2,75), (5,72)]. Done



