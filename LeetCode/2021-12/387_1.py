from collections import defaultdict, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = defaultdict(int)
        
        for i in range(len(s)):
            dict[s[i]] += 1
        
        for key, value in dict.items():
            if value==1:
                return s.index(key)
            
        return -1
    
    def firstUniqChar2(self, s: str) -> int:
        count = Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        
        return -1
    