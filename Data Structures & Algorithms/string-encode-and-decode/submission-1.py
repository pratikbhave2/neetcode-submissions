class Solution:

    def encode(self, strs: List[str]) -> str:

        # Brute force?
        # if not strs:
        #     return ""
        # sizes, res = [], ""
        # for s in strs:
        #     sizes.append(len(s))
        # for sz in sizes:
        #     res += str(sz)
        #     res += ','
        # res += '#'
        # for s in strs:
        #     res += s
        # print(res)
        # return res

        # optimal
        res = ""
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        # Brute force?

        # if not s:
        #     return []

        # sizes, result, i = [], [], 0
        # while s[i] != "#":
        #     curr = ""
        #     while s[i] != ",":
        #         curr += s[i]
        #         i += 1
        #     sizes.append(int(cur))
        #     i += 1
        # i += 1

        # for sz in sizes:
        #     res.append(s[i: i + sz])
        #     i += sz
        # return res

        # Optimal
        res = []
        if not s:
            return res
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        print(res)
        return res
