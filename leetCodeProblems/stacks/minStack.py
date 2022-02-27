"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack:

    def __init__(self):
        self.length = 3 * 10^4
        self.s = list()
        self.minS = list()
        self.top = -1
        self.min = None
        for i in range(0,self.length):
            self.s.append(None)
            self.minS.append(None)


    def push(self, val: int) -> None:
        self.top = self.top + 1
        self.s[self.top] = val


    def empty(self):
        return self.top == -1


    def pop(self) -> None:
        self.top = self.top-1
        return self.s[self.s.top+1]


    def top(self) -> int:
        return self.s[self.s.top]


    def _setMin(self):
        if self.empty():
            self.min = val
        else:
            self.min = None
        for item in self.s:
            if item < self.min:
                self.min = item


    def getMin(self) -> int:
        return self.min


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert -3 == minStack.getMin() # return -3
    minStack.pop()
    assert 0 == minStack.top()    # return 0
    assert -2 == minStack.getMin() # return -2



