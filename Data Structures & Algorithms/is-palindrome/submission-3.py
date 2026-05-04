class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_characters = ["?", "#", "@", "!", ",", "'", ".", ":"]
        word_without_space = s.replace(" ", "").lower()
        for i in word_without_space:
            if i in special_characters:
                word_without_space = word_without_space.replace(i, "").lower()
        firstPointer, secondPointer = 0, len(word_without_space)-1
        while firstPointer < secondPointer:
            if word_without_space[firstPointer]!= word_without_space[secondPointer]:
                return False
            firstPointer+=1
            secondPointer-=1
        return True      