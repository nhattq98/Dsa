class LongestSubString:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            result = max(result, r - l + 1)

        return result


def test():
    lgs = LongestSubString()
    result = lgs.lengthOfLongestSubstring(s="abcabcbb")
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
