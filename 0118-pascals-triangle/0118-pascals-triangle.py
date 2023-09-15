class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        
        for i in range(1, numRows):
            prev_row = output[i-1]
            curr_row = [1]

            for j in range(1, len(prev_row)):
                curr_row.append(prev_row[j-1] + prev_row[j])
            
            curr_row.append(1)            
            output.append(curr_row)

        return output