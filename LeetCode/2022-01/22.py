from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def fun(s, left, right):
            if left<n:
                fun(s+'(', left+1, right)
            if right<left:    
                fun(s+')', left, right+1)
            if len(s)==n*2:
                res.append(s)
                
        res = []
        fun('', 0, 0)
        
        return res
             
if __name__=='__main__':
    Solution().generateParenthesis(3)