"""
622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        

    def enQueue(self, value: int) -> bool:
        

    def deQueue(self) -> bool:
        

    def Front(self) -> int:
        

    def Rear(self) -> int:
        

    def isEmpty(self) -> bool:
        

    def isFull(self) -> bool:
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull
"""

from re import X


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.length = k
        self.Q = []
        for i in range(0,k):
            self.Q.append(None)

    def enQueue(self, value: int) -> bool:
        if self.tail == self.length:
            self.tail = self.head
            self.head = self.length -1
            self.Q[self.tail] = value
            return False
        elif self.tail < self.head:
            self.tail += 1
            self.head += 1
            self.Q[self.tail] = value
            return False
        else:
            self.Q[self.tail] = value
            self.tail += 1
            return True

    def deQueue(self) -> bool:
        if self.tail == 0 and self.head == 0: # Queue is empty, can't remove an item
            return False
        elif self.head == self.length-1:
            self.Q[self.head-1] = None
            self.tail = self.head -1
            self.head = 1
        else:
            self.Q[self.head] = None
            # self.tail -= 1
            if self.tail != self.head:
                self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.tail]

    def Rear(self) -> int:
        return self.Q[self.head]

    def isEmpty(self) -> bool:
        return  self.tail == 0 and  self.head == 0

    def isFull(self) -> bool:
        return self.tail < self.head or self.tail > self.length

if __name__ == "__main__":
    myCircularQueue =  MyCircularQueue(3)
    assert True == myCircularQueue.enQueue(1) # return True
    assert True == myCircularQueue.enQueue(2) # return True
    assert True == myCircularQueue.enQueue(3) # return True
    assert False == myCircularQueue.enQueue(4) # return False
    assert 3 == myCircularQueue.Rear()     # return 3
    assert True == myCircularQueue.isFull()   # return True
    assert True == myCircularQueue.deQueue()  # return True
    assert True == myCircularQueue.enQueue(4) # return True
    assert 4 == myCircularQueue.Rear()     # return 4


    # From submission input/output
    """
    Input:
        ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
        [[6],[6],[],[],[],[5],[],[],[],[],[],[]]
    Expected:
        [null,true,6,6,true,true,5,true,-1,false,false,false]
    """
    myCircularQueue =  MyCircularQueue(6)
    assert True == myCircularQueue.enQueue(6)
    assert 6 == myCircularQueue.Rear()
    assert True == myCircularQueue.deQueue()
    assert True == myCircularQueue.enQueue(5)
    assert 5 == myCircularQueue.Rear()
    assert True == myCircularQueue.deQueue()
    assert -1 == myCircularQueue.Front()
    assert False == myCircularQueue.deQueue()
    assert False == myCircularQueue.deQueue()
    assert False == myCircularQueue.deQueue()


    """
    Input:
        ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
        [[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]
    Expected:
        [null,true,true,true,true,true,true,false,false,0,0,true]
    """
    myCircularQueue =  MyCircularQueue(8)
    assert True == myCircularQueue.enQueue(3)
    assert True == myCircularQueue.enQueue(9)
    assert True == myCircularQueue.enQueue(5)
    assert True == myCircularQueue.enQueue(0)
    assert True == myCircularQueue.deQueue()
    assert True == myCircularQueue.deQueue()
    assert False == myCircularQueue.isEmpty()
    assert False == myCircularQueue.isEmpty()
    assert 0 == myCircularQueue.Rear()
    assert 0 == myCircularQueue.Rear()
    assert True == myCircularQueue.deQueue()






