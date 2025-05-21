class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counter = {}
        for c in magazine:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else: 
                counter[c] -= 1

        return True

if __name__ == '__main__':
    ransomNote = "abb"
    magazine = "bab"
    solution = Solution()
    print(solution.canConstruct(ransomNote, magazine))            