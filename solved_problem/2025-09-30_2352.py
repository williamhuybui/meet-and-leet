class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        #Hash map
        n = len(grid)
        row_count = {}
        for row in grid:
            if tuple(row) not in row_count:
                row_count[tuple(row)] = 1
            else: 
                row_count[tuple(row)] += 1
        #Check col
        ans = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            if tuple(col)in row_count:
                ans += row_count[tuple(col)]
        return ans
