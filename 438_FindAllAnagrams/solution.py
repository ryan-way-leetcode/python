class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(s) < len(p): return []

        ret = []

        d_p = {}

        for c in p:
            if c not in d_p:
                d_p[c] = 0
            d_p[c] += 1
        
        d_s = {}
        for idx in range(len(p)-1):
            if s[idx] not in d_s:
                d_s[s[idx]] = 0
            d_s[s[idx]] += 1
        
        for idx in range(len(p)-1, len(s)):
            if s[idx] not in d_s:
                d_s[s[idx]] = 0
            d_s[s[idx]] += 1

            if d_s == d_p:
                ret.append(idx-(len(p)-1))
            
            d_s[s[idx-(len(p)-1)]] -= 1

            if d_s[s[idx-(len(p)-1)]] == 0:
                del d_s[s[idx-(len(p)-1)]]
        
        return ret