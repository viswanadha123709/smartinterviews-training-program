class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row = col = 0

        while row < m // 2 and col < n // 2:
            temp = []

            for i in range(col, n - col):
                temp.append(grid[row][i])

            for i in range(row + 1, m - row):
                temp.append(grid[i][n - col - 1])

            for i in range(n - col - 2, col - 1, -1):
                temp.append(grid[m - row - 1][i])

            for i in range(m - row - 2, row, -1):
                temp.append(grid[i][col])

            k1 = k % len(temp)
            temp = temp[k1:] + temp[:k1]

            idx = 0

            for i in range(col, n - col):
                grid[row][i] = temp[idx]
                idx += 1

            for i in range(row + 1, m - row):
                grid[i][n - col - 1] = temp[idx]
                idx += 1

            for i in range(n - col - 2, col - 1, -1):
                grid[m - row - 1][i] = temp[idx]
                idx += 1

            for i in range(m - row - 2, row, -1):
                grid[i][col] = temp[idx]
                idx += 1

            row += 1
            col += 1

        return grid