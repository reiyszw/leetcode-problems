class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = []
        num2 = []

        for i in range(1, n + 1):
            if i % m:
                num1.append(i)
            else:
                num2.append(i)

        return sum(num1) - sum(num2)

if __name__ == '__main__':
    n = 10
    m = 3
    solution = Solution()
    print(solution.differenceOfSums(n, m))            