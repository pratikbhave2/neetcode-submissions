class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force
        # n = len(nums)
        # res = [0] * n

        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod

        # return res

        # prefix & suffix
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        print("Result", res)
        print("Prefix", pref)
        print("Suffix", suff)
        print("\n")
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        
        print("After loop 1")
        print(pref)
        print("\n")
        for j in range(n - 2, -1, -1):
            suff[j] = nums[j + 1] * suff[j + 1]

        print("After loop 2")
        print(suff)
        print("\n")
        for i in range(n):
            res[i] = pref[i] * suff[i]

        print("After loop 3")
        print(res)
        print("\n")
        return res