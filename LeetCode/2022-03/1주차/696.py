class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0 
        
        for i in range(len(s)):
            zero_cnt, one_cnt = 0, 0
            if s[i]=='0':
                zero_cnt = 1
            else:
                one_cnt = 1 
            for j in range(i+1, len(s)):
                if s[j]=='0':
                    zero_cnt += 1
                else:
                    one_cnt += 1 
                    
                if zero_cnt == one_cnt:
                    answer += 1
                    break
        return answer
    
    def countBinarySubstrings2(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1]==s[i]:
                groups[-1]+=1
            else:
                groups.append(1)
        
        answer = 0 
        for i in range(1, len(groups)):
            answer += min(groups[i-1], groups[i])
            
        return answer    
    
    def countBinarySubstrings3(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev, cur = cur, 1
                
        return ans+min(prev, cur)
        
if __name__=='__main__':
    mysolution()