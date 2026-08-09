class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_dict = {}
        for i, item in enumerate(s):
            count_dict[item] = 1 + count_dict.get(item, 0)
        
        for i, item in enumerate(t):
            if item not in count_dict or count_dict[item] == 0:
                return False
            count_dict[item] -= 1
        
        return True
