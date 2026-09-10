class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for word in strs:

            sorted_text = "".join(sorted(word))

            if sorted_text in hashmap:
                hashmap[sorted_text].append(word)
            else:
                hashmap[sorted_text] = [word]
        
        
        return list(hashmap.values())
