class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = -1
        for sentence in sentences:
            most = max(most, len(sentence.split(' ')))

        return most