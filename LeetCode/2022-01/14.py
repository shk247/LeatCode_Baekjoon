from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x:len(x))
        answer = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            for j in range(len(answer)):
                if str[j] != answer[j]:
                    answer = answer[:j]
                    if not answer:
                        break
                    break
        return ''.join(answer) 
    
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i==len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
                
        return strs[0]
                
if __name__=='__main__':
    print(Solution().longestCommonPrefix2(["flower","fl","flight"]))