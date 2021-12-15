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
                
        print(len(answer))
        
if __name__=='__main__':
    Solution().lengthOfLongestSubstring("abcabcbb")