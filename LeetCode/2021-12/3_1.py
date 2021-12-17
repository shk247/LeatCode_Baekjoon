from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        answer = 0 
        for i in range(len(s)):
            tmp = ''
            for j in range(i, len(s)):
                if s[j] in tmp:
                   answer = max(answer, len(tmp))
                   break 
                tmp += s[j]
            else:
                answer = max(answer, len(tmp))
                
        return answer

    def lengthOfLongestSubstring2(self, s: str) -> int:
        answer = 0 
        left = 0 
        l = {} 
        
        for idx, c in enumerate(s):
            if c in l and left<=l[c]:
                left = l[c]+1
            else:
                answer = max(answer, idx-left+1)
            l[c] = idx
        
        return answer

if __name__=='__main__':
    print(Solution().lengthOfLongestSubstring(""))