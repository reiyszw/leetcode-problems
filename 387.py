class Solution(object):
    def firstUniqChar(self, s):
        hashMap = {}

        for i, c in enumerate(s):
            if not c in hashMap:
                hashMap[c] = 1
            else:
                hashMap[c] += 1

        for i, c in enumerate(s):
            if hashMap[c] == 1:
                return i
        return - 1

if __name__ == '__main__':
    s = "aabb"
    solution = Solution()
    print(solution.firstUniqChar(s))            