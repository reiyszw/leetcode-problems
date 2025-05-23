class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        total = 0

        for h in hours: 
            if h >= target:
                total += 1

        return total

if __name__ == '__main__':
    hours = [0,1,2,3,4]
    target = 2
    solution = Solution()
    print(solution.numberOfEmployeesWhoMetTarget(hours, target))            