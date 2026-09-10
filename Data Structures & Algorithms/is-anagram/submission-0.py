class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table_s = {}
        hash_table_t = {}

        for c in s:
            if c in hash_table_s:
                hash_table_s[c] += 1
            else:
                hash_table_s[c] = 1

        for c in t:
            if c in hash_table_t:
                hash_table_t[c] += 1
            else:
                hash_table_t[c] = 1
        

        return hash_table_s == hash_table_t
            
        