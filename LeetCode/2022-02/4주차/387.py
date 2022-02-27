from collections import defaultdict
import collections
import enum

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = defaultdict(int)
        
        for char in s:
            dict[char]+=1
            
        for i in range(len(s)):
            if dict[s[i]]==1:
                return i
            
        return -1 
    
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for idx, s in enumerate(s):
            if count[s]==1:
                return idx
        
        return -1 