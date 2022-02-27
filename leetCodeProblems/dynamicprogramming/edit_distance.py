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
        # Create a table to store results of subproblems
        table, m, n = self.buildDefaultTable(word1, word2)
    
        # Fill d[][] in bottom up manner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If last characters are same, ignore last char
                # and recur for remaining string
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
    
                # If last character are different, consider all
                # possibilities and find minimum
                else:
                    table[i][j] = 1 + min(table[i][j-1],    # Insert
                                    table[i-1][j-1],        # Replace
                                    table[i-1][j])          # Delete
        return table[m][n]


    def buildDefaultTable(self, word1: str, word2: str):
        m = len(word1)
        n = len(word2)

        table = [[0 for x in range(0, n+1)] for x in range(0, m+1)]

        for i in range(0, m + 1):
            # If second string is empty, only option is to
            # remove all characters of second string
            table[i][0] = i    # Min. operations = i

        for j in range(0, n + 1):
            # If first string is empty, only option is to
            # insert all characters of second string
            table[0][j] = j    # Min. operations = j
        return table, m, n


if __name__ == "__main__":
    s = Solution()
    word1 = "sunday"
    word2 = "saturday"

    assert 3 == s.minDistance("horse", "ros")
    assert 5 == s.minDistance("intention", "execution")
    assert 1 == s.minDistance("horse", "rorse")
    assert 4 == s.minDistance("int", "integer")
