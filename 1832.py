class Solution(object):
    ALPHABET_CHARACTERS_COUNT = 26

    def checkIfPangram(self, sentence):
        if len(sentence) < self.ALPHABET_CHARACTERS_COUNT:
            return False
        
        sett = set()

        for i in sentence:
            sett.add(i)

        if len(sett) == self.ALPHABET_CHARACTERS_COUNT:
            return True
        else: 
            return False

        # if len(sentence) < 26:
        #     return False
        
        # sett = set()

        # sett= {'a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

        # for s in sentence:
        #     if s in sett:
        #         sett.remove(s)

        # if not len(sett):
        #     return True
        
        # return False

if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    solution = Solution()
    print(solution.checkIfPangram(sentence))            