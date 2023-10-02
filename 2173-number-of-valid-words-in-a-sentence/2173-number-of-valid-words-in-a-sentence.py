class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile(r'(^[a-z]+(-[a-z]+)?)?[,.!]?$')
        return sum(bool(pattern.match(word)) for word in sentence.split())