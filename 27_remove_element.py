class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums[:k])
        return k

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    print(solution.removeElement(nums, val))