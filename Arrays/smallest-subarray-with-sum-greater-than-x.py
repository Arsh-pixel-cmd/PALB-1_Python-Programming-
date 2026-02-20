class Solution:
    def smallestSubWithSum(self, x, a):
        n = len(a)
        min_len = n + 1
        curr_sum = 0
        start = 0

        for end in range(n):
            curr_sum += a[end]

            while curr_sum > x:
                min_len = min(min_len, end - start + 1)
                curr_sum -= a[start]
                start += 1

        return 0 if min_len == n + 1 else min_len
