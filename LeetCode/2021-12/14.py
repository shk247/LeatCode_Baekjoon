from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        idx = 0
        while len(strs[0])>idx:
            tmp = strs[0][idx]
            for i in range(1, len(strs)):
                if len(strs[i])<=idx or strs[i][idx] != tmp:
                    break
            else:
                answer += tmp
                idx += 1
                continue
            break
        return answer
    
    def Horizontalscanning(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) == -1:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
    def Verticalscanning(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i==len(strs[j]) or strs[j].find(c) == -1:
                     return strs[0][:i]
        return strs[0]
        
                
if __name__=='__main__':
    print(Solution().Horizontalscanning(["flower","flow","flight"]))