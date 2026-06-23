class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_hashmap = {} # sorted(string) : indeces

        for i in range(0, len(strs)):
            sorted_str_list = sorted(strs[i])
            sorted_str = ''.join(sorted_str_list)
            if sorted_str in anagram_hashmap:
                anagram_hashmap[sorted_str].append(i)
            else:
                anagram_hashmap[sorted_str] = [i]

        output = []
        temp = []
        for _, s in enumerate(anagram_hashmap):
            for index in anagram_hashmap[s]:
                temp.append(strs[index])
            output.append(temp)
            temp = []
        return output
            