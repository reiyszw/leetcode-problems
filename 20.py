class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

if __name__ == '__main__':
    # s = "()[]{}"
    s = "([])"
    solution = Solution()
    print(solution.isValid(s))            