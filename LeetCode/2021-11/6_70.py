class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(0, n)

    def climb(self, i, n):
        if i>n:
            return 0
        if i == n:
            return 1
        return self.climb(i+1, n) + self.climb(i+2,n)

    def climbStairs2(self, n: int) -> int:
        answer = [0 for _ in range(n)]
        return self.climb2(0, n, answer)

    def climb2(self, i, n, answer):
        if i>n:
            return 0

        if i == n:
            return 1

        if answer[i]>0:
            return answer[i]

        answer[i] = self.climb2(i+1, n, answer) + self.climb2(i+2, n, answer)
        
        return answer[i]

    def climbStairs3(self, n: int) -> int:
        if n==1:
            return 1
        first = 1
        second = 2
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second


if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs2(5))
