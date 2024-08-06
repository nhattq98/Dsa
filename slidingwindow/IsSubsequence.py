# https://leetcode.com/problems/is-subsequence
class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" and t == "": return True
        if t == "": return False

        len_s = len(s)
        len_t = len(t)
        i = 0
        j = 0

        while i < len_s:
            print(s[i])
            while j < len_t:
                if j >= len_t - 1:
                    if i == len_s - 1 and s[i] == t[j]:
                        return True
                    return False
                if s[i] == t[j]:
                    i += 1
                    j += 1
                    break
                else:
                    j += 1

        return True


def test():
    isSubsequence = IsSubsequence()
    result = isSubsequence.isSubsequence(s="abc", t="ahbgdc")
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
