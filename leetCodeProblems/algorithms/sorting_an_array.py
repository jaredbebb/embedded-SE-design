"""
912. Sort an Array
Medium

1836

500

Add to List

Share
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""

import sys
import math


class List(list):
    pass

class Solution:
    def sortArray(self, nums):
        """
        Insertion Sort
        """
        # return self.insertionSort(nums)

        """
        Merge Sort
        """
        p = 0
        r = len(nums)-1
        nums = self.mergeSort(nums, p, r)
        return nums

    def mergeSort(self, nums, p, r):
        if p < r:
            q =  math.floor( ( p + r ) / 2)
            self.mergeSort(nums, p,q)
            self.mergeSort(nums, q+1, r)
            self.merge(nums, p, q, r)
        return nums

    def merge(self, nums, p, q, r):
        """
        MERGE(A, p, q, r) CLRS p. 31
        A == nums
        p, q, r are indices into the array such that
        p <= q < r
        """

        n1 = q - p + 1
        n2 = r - q

        L = [sys.maxsize] * (n1+1)
        R = [sys.maxsize] * (n2+1)

        # Fill temp arrays with nums
        for i in range(0, n1):
            L[i] = nums[p+i]
        for j in range(0,n2):
            R[j] = nums[q + j + 1]

        i = 0
        j = 0

        for k in range(p, r+1):
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                 nums[k] = R[j]
                 j+=1
            k += 1

    def insertionSort(self, nums):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    temp_i = nums[i]
                    temp_j = nums[j]
                    nums[i] = temp_j
                    nums[j] = temp_i
        return nums

if __name__ == "__main__":
    ex1 = ([5,2,3,1], [1,2,3,5])
    ex2 = ([5,1,1,2,0,0], [0,0,1,1,2,5])
    ex3 = ([5,2,4,7,1,3,2,6], [1,2,2,3,4,5,6,7])
    
    s = Solution()
    s.sortArray(ex1[0])
    assert ex1[0] == ex1[1]

    solution = s.sortArray(ex2[0])
    assert solution == ex2[1]

    s.sortArray(ex3[0])
    assert ex3[0] == ex3[1]

