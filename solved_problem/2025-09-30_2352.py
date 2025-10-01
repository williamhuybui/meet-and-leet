class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        row_count = {}
        for row in grid:
            if tuple(row) not in row_count:
                row_count[tuple(row)] = 1
            else: 
                row_count[tuple(row)] += 1
        print("Row Tuple and frequency", row_count)
        #Tranpose
        print("Before tranpose", grid)
        for i in range(n):
            for j in range(i + 1, n):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        print("After tranpose", grid)
        #Check col
        ans = 0
        for col in grid:
            if tuple(col)in row_count:
                ans += row_count[tuple(col)]
        return ans
