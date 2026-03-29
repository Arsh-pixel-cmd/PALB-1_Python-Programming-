def max_people_visible(heights):
    n = len(heights)
    res = [0] * n
    stack = []
    
    for i in range(n - 1, -1, -1):
        while stack and heights[i] > stack[-1]:
            res[i] += 1
            stack.pop()
        if stack:
            res[i] += 1
        stack.append(heights[i])
    return res

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter heights: ").split()]
    # This problem requires seeing people in front and back in the screenshot description
    # "at most one person taller blocks the view"
    # The leetcode version is "can see i if no one height[k] >= height[i]"
    # I'll implement a bidirectional check as per screenshot
    def bidirectional_visible(h):
        n = len(h)
        res = [0] * n
        for i in range(n):
            # See forward
            tallest = -1
            for j in range(i + 1, n):
                res[i] += 1
                if h[j] >= h[i]:
                    break
            # See backward
            for j in range(i - 1, -1, -1):
                res[i] += 1
                if h[j] >= h[i]:
                    break
        return res
        
    print(f"Visible counts: {bidirectional_visible(arr)}")
