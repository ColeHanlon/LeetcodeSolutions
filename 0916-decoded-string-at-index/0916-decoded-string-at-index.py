class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        if len(s) == 0:
            return ""
        
        decoded_size = [1]

        for char in s[1:]:
            if char.isalpha():
                decoded_size.append(decoded_size[-1] + 1)
            else:
                decoded_size.append(decoded_size[-1] * int(char))
                    
            if decoded_size[-1] > k-1:
                break

        for i in range(len(decoded_size)-1, -1, -1):
            print(i)
            k %= decoded_size[i]
            if k == 0 and s[i].isalpha():
                return s[i]
        
        return ""

        