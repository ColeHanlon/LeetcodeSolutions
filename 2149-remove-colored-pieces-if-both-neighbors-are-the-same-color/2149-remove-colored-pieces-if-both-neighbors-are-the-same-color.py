class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_moves = 0
        b_moves = 0
        i = 0
        while i < len(colors):
            curr_chain = 0
            while i < len(colors) and colors[i] == 'A':
                print(i)
                curr_chain += 1
                i += 1

            if curr_chain > 2:
                a_moves += curr_chain - 2

            curr_chain = 0
            while i < len(colors) and colors[i] == 'B':
                curr_chain += 1
                i += 1

            if curr_chain > 2:
                b_moves += curr_chain - 2
            
        return a_moves > b_moves