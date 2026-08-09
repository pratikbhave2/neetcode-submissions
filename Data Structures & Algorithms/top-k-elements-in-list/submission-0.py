class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # rev_sorted = sorted(nums)
        
        # count_map = {}
        # topK = []
        # for item in rev_sorted:
        #     if item in count_map:
        #         count_map[item] += 1
        #     else:
        #         count_map[item] = 1

        #     if len(topK) < k and item not in topK:
        #         topK.append(item)

        # Brute force

        countMap = {}
        keys = []
        counts = []
        
        for item in nums:
            if item not in countMap:
                countMap[item] = nums.count(item)
            if item not in keys:
                keys.append(item)
                counts.append(nums.count(item))

        topK = [x for _, x in sorted(zip(counts, keys), reverse=True)]

        return topK[:k]
        # How to find top "K" elements now
        
        # for num, count in countMap.items():
            
