from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for num in range(n+1):
            cnt = 0 
            while num!=0:
                num, r = divmod(num, 2)
                cnt+=r
            answer.append(cnt)
        return answer