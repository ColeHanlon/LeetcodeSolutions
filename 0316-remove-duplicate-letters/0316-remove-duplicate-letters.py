class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # aba 
        positions = defaultdict(list)

        for i in range(len(s)):
            positions[s[i]].append(i)

        output = []
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                while output and output[-1] > s[i] and positions[output[-1]][-1] > i:
                    seen.remove(output[-1])
                    output.pop()
                
                seen.add(s[i])
                output.append(s[i])
    
        return ''.join(output)