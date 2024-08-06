class SimplifyPath:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split = path.split("/")
        for item in split:
            if item.strip() != "":
                print(item)
                stack.append(item)

        result = ""
        count = 0
        while len(stack) != 0:
            s = stack.pop()

            if s == "..":
                count = count + 1
            elif s == ".":
                continue
            else:
                if count == 0:
                    result = "/" + s + result
                else:
                    count = count - 1

        if result == "":
            return "/"
        else:
            return result

def test():
    sp = SimplifyPath()
    str = "/.../a/../b/c/../d/./"
    result = sp.simplifyPath(str)
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
