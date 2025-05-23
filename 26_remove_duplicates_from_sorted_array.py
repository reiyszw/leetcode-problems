class Solution(object):
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    print(solution.removeDuplicates(nums))            