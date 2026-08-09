class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## Naive solution"
        ## Sort each string, group them using a hashmap
        anagram_map = {}
        for i, each_str in enumerate(strs):
            sorted_str = "".join(sorted(each_str))
            # print(sorted_str)
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = [i]
            else:
                anagram_map[sorted_str].append(i)
    
        output = []
        for ana, indices in anagram_map.items():
            group = []
            print(ana, indices)
            for index in indices:
                group.append(strs[index])
            output.append(group)
    
        return output