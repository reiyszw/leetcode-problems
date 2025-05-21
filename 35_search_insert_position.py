class Solution(object):
   def searchInsert(self, nums, target):
       n = len(nums)
       l = 0
       r = n - 1

       while l <= r:
           m = (l + r) // 2

           if nums[m] < target:
               l = m + 1
           elif nums[m] > target:
               r = m - 1
           else:
               return m
       return l 

if __name__ == '__main__':
    nums = [1,3,5,6,8,9]
    target = 4
    solution = Solution()
    print(solution.searchInsert(nums, target))            