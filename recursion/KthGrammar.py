# ref: https://leetcode.com/problems/k-th-symbol-in-grammar/description/
class KthGrammar:
    def kthGrammar(self, n: int, k: int):
        if n == 1: return 0
        length = 2 ** (n - 1)
        mid = length // 2
        if k < mid:
            return self.kthGrammar(n - 1, k)
        else:
            return int(not self.kthGrammar(n - 1, k - mid))

    def kthGrammarNotOptimal(self, n: int, k: int):
        nRowResult = self.nRow(n)
        kth = nRowResult[k - 1]
        return kth

    def nRow(self, n: int) -> "":
        if n == 1:
            return "0"

        inRow = self.nRow(n - 1)
        result = ""
        for char in inRow:
            if char == "0":
                result += "01"
            else:
                result += "10"

        return result


def test():
    kthGrammar = KthGrammar()
    nRow = kthGrammar.kthGrammar(n=30, k=434991989)
    print("nRow is " + nRow)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
