class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        res = []

        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                val = arr1[i]
                res.append(val)

                while i < n1 and arr1[i] == val:
                    i += 1
                while j < n2 and arr2[j] == val:
                    j += 1
                while k < n3 and arr3[k] == val:
                    k += 1

            else:
                mn = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == mn:
                    i += 1
                elif arr2[j] == mn:
                    j += 1
                else:
                    k += 1

        return res if res else [-1]
