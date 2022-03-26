class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # self.stack.append(val)
        if not self.stack:
            self.stack.append([val, val])
            return
        min_value = self.stack[-1][1]
        self.stack.append([val, min(val, min_value)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        # answer = -1e9
        # for num in self.stack:
        #     if num<answer:
        #         answer=num
        # return answer
        return self.stack[-1][1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()