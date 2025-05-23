class Solution(object):
    def majorityElement(self, nums):
        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res

if __name__ == '__main__':
    nums = [2,2,3,3,3]
    solution = Solution()
    print(solution.majorityElement(nums))            