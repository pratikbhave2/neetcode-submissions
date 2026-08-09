class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute Force
        n1 = len(nums1)
        n2 = len(nums2)

        merged = nums1 + nums2
        merged.sort()

        total_n = len(merged)

        if total_n %2 == 0:
            return (merged[total_n // 2 - 1] + merged[total_n // 2]) / 2.0
        else:
            return merged[total_n // 2]

        