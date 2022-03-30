from itertools import product 
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        nums = []
        for d in digits:
            nums.append(dict[d])
            
        l = list(product(*nums))
        answer = []
        for i in l:
            answer.append(''.join(i))
        
        return answer
    
    def letterCombinations2(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        
        def dfs(idx, s):
            if len(s)==len(digits):
                result.append(s)
                return
            
            for i in range(idx, len(digits)):
                for j in dict[digits[i]]:
                    dfs(i+1, s+j)
                    
        dfs(0, '')
        
        return result
    
    def letterCombinations3(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = list(dict[digits[0]])
        
        for digit in digits[1:]:
            tmp = []
            for r in result:
                for d in list(dict[digit]):
                    tmp.append(r+d)
            result = tmp
        
        return result
        
if __name__=='__main__':
    Solution().letterCombinations3("23")
    