class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        
        current_sum = 0
        while 0 < num:
            current_sum += num % 10
            num = num // 10

        return self.addDigits(current_sum)

if __name__ == '__main__':
    num = 38
    solution = Solution()
    print(solution.addDigits(num))            