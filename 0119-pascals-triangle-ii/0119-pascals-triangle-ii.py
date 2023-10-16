class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
       final_row = [1]
       for _ in range(rowIndex):
           temp_row = [0] + final_row + [0]
           final_row = []
           for i in range(len(temp_row) - 1):
               final_row.append(temp_row[i] + temp_row[i + 1])

       return final_row