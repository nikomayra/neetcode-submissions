class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anag_hash = {}

        for word in strs:

            sorted_word = str(sorted(word))

            if sorted_word in anag_hash:
                anag_hash[sorted_word].append(word)
            else:
                anag_hash[sorted_word] = [word]

        return list(anag_hash.values())