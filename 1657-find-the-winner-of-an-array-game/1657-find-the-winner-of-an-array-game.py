class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        most_wins = 0
        element = -1
        while most_wins < k:
            if (arr[0] > arr[1]):
                element = arr[0]
                most_wins += 1
                arr.append(arr[1])
                del arr[1]
            else:
                element = arr[1]
                most_wins = 1
                arr.append(arr[0])
                arr[0] = arr[1]
                del arr[1]

        return element
        