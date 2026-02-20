class Solution:
    def findMinDiff(self, A, M):
        n = len(A)
        if M == 0 or M > n:
            return 0

        A.sort()
        min_diff = float('inf')

        for i in range(n - M + 1):
            diff = A[i + M - 1] - A[i]
            min_diff = min(min_diff, diff)

        return min_diff
