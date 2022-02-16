"""
706. Design HashMap
https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

 - MyHashMap() initializes the object with an empty map.
 - void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
 - int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
 - void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

"""

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
            self.T.append(list())

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        index = self.hash(key)
        # update value if key exists
        try:
            i, j = self.search(key, get_indexes=True)
        except KeyError:
            self.T[index].append((key,value)) 
            return
        self._update(key, value, i, j)

    def _update(self, key, value, i, j):
        self.T[i][j] = (key, value)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            val = self.search(key)
        except KeyError:
            return -1
        return val
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        pass

    def hash(self, key):
        """
        CLRS p. 263
        The division method
        """
        if type(key) == str:
            # convert string to int
            num_repr = int(key, base=36)
        else:
            num_repr =  key
        return num_repr % self.m

    def search(self, key, get_indexes = False):
        i = self.hash(key)
        j = 0
        key_not_found = True
        while key_not_found:
            try:
                key_not_found = self.T[i][j][0] != key
            except IndexError:
                raise KeyError
            if not key_not_found:
                break
            j += 1
        if get_indexes:
            return i, j
        else:
            return self.T[i][j][1]

    def keys(self):
        return self.iteritems(0)

    def values(self):
        return self.iteritems(1)

    def iteritems(self, item):
        """
        specify item=0 item=1 to designate keys or values
        """
        items = set()
        for L in self.T:
            for t in L:
                items.add(t[item])
        return items


        

if __name__ == "__main__":

    # Your MyHashMap object will be instantiated and called as such:
    # obj = MyHashMap()
    # obj.put(key,value)
    # param_2 = obj.get(key)
    # obj.remove(key)

    key = "a"
    value = 1

    myHashMap = MyHashMap()
    myHashMap.put(key,value)

    assert value ==  myHashMap.get(key)
    myHashMap.remove(key)

    # Tests from problem example #1
    myHashMap = MyHashMap()
    myHashMap.put(1, 1); # The map is now [[1,1]]

    assert set([1]) == myHashMap.keys()
    assert set([1]) == myHashMap.values()

    myHashMap.put(2, 2); # The map is now [[1,1], [2,2]]
    assert set([1,2]) == myHashMap.keys()
    assert set([1,2]) == myHashMap.values()

    assert 1 == myHashMap.get(1);    # return 1, The map is now [[1,1], [2,2]]
    assert -1 == myHashMap.get(3);    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]

    myHashMap.put(2, 1); # The map is now [[1,1], [2,1]] (i.e., update the existing value)

    assert set([1,2]) == myHashMap.keys()
    assert set([1,1]) == myHashMap.values()

    assert 1 == myHashMap.get(2);    # return 1, The map is now [[1,1], [2,1]]
    myHashMap.remove(2); # remove the mapping for 2, The map is now [[1,1]]
    
    assert set([1]) == myHashMap.keys()
    assert set([1]) == myHashMap.values()

    assert -1 == myHashMap.get(2);    # return -1 (i.e., not found), The map is now [[1,1]]

