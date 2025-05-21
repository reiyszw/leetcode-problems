class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while j <= len(t) - 1:
            if i < len(s) and t[j] == s[i]:
                i += 1
            j += 1
        return i == len(s)
        
if __name__ == '__main__':
    s = "b"
    t = "abc"
    solution = Solution()
    print(solution.isSubsequence(s, t))            