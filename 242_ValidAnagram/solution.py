class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}

        for c in s:
            if c not in d_s:
                d_s[c] = 0
            d_s[c] += 1

        for c in t:
            if c not in d_t:
                d_t[c] = 0
            d_t[c] += 1

        return d_t == d_s