class Solution(object):
    def sumOfMultiples(self, n):
        total = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i 
        return total

if __name__ == '__main__':
    n = 7
    solution = Solution()
    print(solution.sumOfMultiples(n))            