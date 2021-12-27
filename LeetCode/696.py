class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(s)
        ans = 0 
        for i in range(len(s)):
            cnt = 0 
            for j in range(i, len(s)):
                if s[j]=='1':
                    cnt += 1
                else:
                    cnt -= 1
                    
                if cnt == 0:
                    ans +=1
                    break
        return ans
    
    def countBinarySubstrings2(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
        ans = 0 
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
    
    def countBinarySubstrings3(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans + min(prev, cur)
        
    
if __name__=='__main__':
    print(Solution().countBinarySubstrings2("101010"))