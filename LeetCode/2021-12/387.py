from collections import defaultdict, Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = defaultdict(int)
        s = list(s)
        for i in s:
            dict[i] += 1
        for str, cnt in dict.items():
            if cnt == 1:
                return s.index(str)
        return -1

    def firstUniqChar2(self, s: str) -> int:
        
        count = Counter(s)
        
        for idx, alph in enumerate(s):
            if count[alph] == 1:
                return idx
        return -1 
        
        

if __name__=='__main__':
    Solution().firstUniqChar2("dddccdbba")