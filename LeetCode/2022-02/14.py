import sys 
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = strs[0]
        for i in range(1, len(strs)):
            str = strs[i]
            for j in range(len(str)):
                if len(answer)>j:
                    if answer[j] != str[j]:
                        if j==0:
                            return ''
                        else:
                            answer = str[:j]
                        break
                else:
                    break
            else:
                answer = str
        return answer
    
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) == -1:
                prefix = prefix[:-1]
                if prefix=='':
                    return prefix
        return prefix
    
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i==len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
        
    
if __name__=='__main__':
    print(Solution().longestCommonPrefix3(["flower","flow","flight"]))