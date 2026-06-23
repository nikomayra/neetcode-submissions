class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            ss = ''.join(sorted(s))
            if ss in hashmap:
                hashmap[ss].append(s)
            else:
                hashmap[ss] = [s]
        return list(hashmap.values())
