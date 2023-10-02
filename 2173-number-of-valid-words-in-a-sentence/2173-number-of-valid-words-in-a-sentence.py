class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(bool(re.compile(r'(^[a-z]+(-[a-z]+)?)?[,.!]?$').match(word)) for word in sentence.split())