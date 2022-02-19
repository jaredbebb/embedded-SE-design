"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = self.initializeZeros(len(word1), len(word2))
        table = self.calc_table(table,word1, word2)
        dist = self.calcDistance(table)
        return dist

    def initializeZeros(self, len1, len2):
        table = []
        for i in range(0,len2):
            table.append([])
            for j in range(0,len1):
                table[i].append(0)
        return table

    def calc_table(self, table, word1: str, word2: str):
        for i in range(0,len(word1)-1):
            for j in range(0, len(word2)-1):
                table[j][i] = int(word1[i] != word2[j])
        return table

    def calcDistance(self, table):
        dist = 0
        for i in range( max( len(table), len(table[0]))):
            dist+= table[i][i]
        return dist


if __name__ == "__main__":
    s = Solution()
    assert 1 == s.minDistance("horse", "rorse")
    assert 5 == s.minDistance("intention", "execution")
    assert 4 == s.minDistance("int", "integer")

