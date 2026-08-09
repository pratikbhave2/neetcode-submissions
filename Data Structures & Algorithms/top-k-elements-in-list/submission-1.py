class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

            
        # # Brute force
        # keys = []
        # counts = []

        # # O(n * nlogn) time, O (2 * n) space        
        # for item in nums:
        #     if item not in keys:
        #         keys.append(item)
        #         counts.append(nums.count(item))

        # topK = [x for _, x in sorted(zip(counts, keys), reverse=True)]

        # return topK[:k]

            
        # Smart solution
        counts = {}
        freq =[[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        for n, c in counts.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
