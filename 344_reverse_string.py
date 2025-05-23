class Solution(object):
    def reverseString(self, s):
        j = len(s) - 1
        middle = (0 + j) // 2
        for i, _ in enumerate(s):
            if i < middle:
                s[i], s[j] = s[j], s[i]
                j -= 1   
        return s
        # l, r = 0, len(s) - 1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1
        # return s

if __name__ == '__main__':
    s = ["h","e","l","l","o"]   
    solution = Solution()
    print(solution.reverseString(s))            