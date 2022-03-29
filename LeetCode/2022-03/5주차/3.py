class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        for i in range(len(s)):
            tmp = ''
            for j in range(i, len(s)):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            if answer<len(tmp):
                answer = len(tmp)
        return answer
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        answer = 0 
        sub = ''
        
        for char in s:
            if char not in sub:
                sub += char
                answer = max(answer, len(sub))
            else:
                idx = sub.index(char)
                sub = sub[idx+1:] + char
                
        return answer
    
    def lengthOfLongestSubstring3(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}

        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans
                
if __name__=='__main__':
    Solution().lengthOfLongestSubstring3("abba")