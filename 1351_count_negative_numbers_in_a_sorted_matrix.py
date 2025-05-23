class Solution(object):
    def countNegatives(self, grid):
        m = len(grid)
        n = len(grid[0])
        count = 0
        for row in range(0, m):
            if grid[row][m - 1] >= 0: continue
            elif grid[row][0] < 0:
                count += n * (m - row)
                break
            else:
                left = 0
                right = n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if grid[row][mid] < 0: right = mid - 1
                    else: left = mid + 1
                count += n - left
        return count

if __name__ == '__main__':
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    solution = Solution()
    print(solution.countNegatives(grid))            