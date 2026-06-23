class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            ss = ''.join(sorted(s))
            hashmap[ss].append(s)
        return list(hashmap.values())
