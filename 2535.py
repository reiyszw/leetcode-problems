class Solution(object):
    def differenceOfSum(self, nums):
        elements_sum = sum(nums)
        digits_sum = 0

        for num in nums:
            while num > 0:
                d = num % 10
                digits_sum += d
                num //= 10

        return abs(elements_sum - digits_sum)

if __name__ == '__main__':
    nums = [1,15,6,3]   
    solution = Solution()
    print(solution.differenceOfSum(nums))            