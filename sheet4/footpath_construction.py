def calculate_footpath_cost(n, m, matrix, queries):
    results = []
    for r, c in queries:
        # Convert to 0-based indexing
        r, c = r - 1, c - 1
        
        # This divides the matrix into up to 4 sections
        # Based on the screenshot, it's the sum of minimums of the sections
        # formed by the row and column footpath.
        
        # Remaining sections:
        # Section 1: (0,0) to (r-1, c-1)
        # Section 2: (0, c+1) to (r-1, m-1)
        # Section 3: (r+1, 0) to (n-1, c-1)
        # Section 4: (r+1, c+1) to (n-1, m-1)
        
        sections = []
        # Top-Left
        s1 = [matrix[i][j] for i in range(r) for j in range(c)]
        if s1: sections.append(min(s1))
        
        # Top-Right
        s2 = [matrix[i][j] for i in range(r) for j in range(c+1, m)]
        if s2: sections.append(min(s2))
        
        # Bottom-Left
        s3 = [matrix[i][j] for i in range(r+1, n) for j in range(c)]
        if s3: sections.append(min(s3))
        
        # Bottom-Right
        s4 = [matrix[i][j] for i in range(r+1, n) for j in range(c+1, m)]
        if s4: sections.append(min(s4))
        
        results.append(sum(sections))
    return results

if __name__ == "__main__":
    n, m = 3, 3
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    queries = [[2, 2]]
    print(f"Footpath costs: {calculate_footpath_cost(n, m, matrix, queries)}")
