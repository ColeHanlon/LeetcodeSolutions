class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = []

        for letter in t:
            letters.append(letter)
        
        for letter in s:
            letters.remove(letter)

        return letters[0]