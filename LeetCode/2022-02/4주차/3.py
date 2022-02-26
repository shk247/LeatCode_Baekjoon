class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0 
        
        answer = 0
        
        for i in range(len(s)):
            tmp = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    answer = max(answer, len(tmp))
                    break
            else:
                answer = max(answer, len(tmp))
        return answer
    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        answer = 0 
        tmp = ''
        
        for char in s:
            if char not in tmp:
                tmp += char
                answer = max(answer, len(tmp))
            else:
                idx = tmp.index(char)
                tmp = tmp[idx+1:]
        
        return answer

if __name__=='__main__':
    print(Solution().lengthOfLongestSubstring(" "))