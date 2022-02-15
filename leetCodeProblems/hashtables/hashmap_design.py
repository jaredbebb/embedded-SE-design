from numpy import array
import numpy as np


class MyHashMap(object):

    def __init__(self):
        """
        CLRS 258 chaining
        """
        # size of the the list T
        self.m = 701
        self.T = list()
        for i in range(0,self.m):
            self.T.append(None)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        index = self.hash(key)

        # create new list at index if not exist
        if self.T[index] == None:
            self.T[index] = list()
        self.T[index].append((key,value))

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.search(key)
        return val
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        pass

    def hash(self, k):
        """
        CLRS p. 263
        The division method
        """
        # convert string to int
        num_repr = int(key, base=36)
        return num_repr % self.m

    def search(self, k):
        index = self.hash(key)
        i = 0
        while self.T[index][i][0] != key:
            i+=1
        return self.T[index][i][1]

        

if __name__ == "__main__":

    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)

    key = "a"
    value = 1

    obj = MyHashMap()
    obj.put(key,value)

    assert value ==  obj.get(key)
    obj.remove(key)

