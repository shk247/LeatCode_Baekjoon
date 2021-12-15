class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        answer = ''
        for i in range(len(s)):
            tmp = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            if len(answer)<=len(tmp):
                answer = tmp
                
        return len(answer)
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        ans = 0 
        left = 0 
        used = {}
        
        for idx, c in enumerate(s):
            if c in used and left <= used[c]:
                left = used[c] + 1
            else:
                ans = max(ans, idx-left+1)
            used[c] = idx
        
        return ans
    
if __name__=='__main__':
    Solution().lengthOfLongestSubstring3(" ")