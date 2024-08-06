# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class CircularGame:
    # time complexity is o(n2)
    def findTheWinner_approach01(self, n: int, k: int) -> int:
        arr = [i + 1 for i in range(n)]

        def helper(arr, startIndex):
            # base case
            if len(arr) == 1:
                return arr[0]

            # recursive case
            indexToRemove = (startIndex + k - 1) % len(arr)
            del arr[indexToRemove]
            return helper(arr, indexToRemove)

        return helper(arr, 0)


def test():
    circularGame = CircularGame()
    result = circularGame.findTheWinner_approach01(n=5, k=2)
    print("result " + result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
