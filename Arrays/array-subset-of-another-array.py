class Solution:
    def isSubset(self, a, b):
        freq = {}

        for x in a:
            freq[x] = freq.get(x, 0) + 1

        for x in b:
            if x not in freq or freq[x] == 0:
                return False
            freq[x] -= 1

        return True
