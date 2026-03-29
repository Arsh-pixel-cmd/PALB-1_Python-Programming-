def calculate_2d_prefix_sum(matrix, queries):
    rows, cols = len(matrix), len(matrix[0])
    # Build 2D prefix sum array
    ps = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            ps[r+1][c+1] = matrix[r][c] + ps[r][c+1] + ps[r+1][c] - ps[r][c]
            
    results = []
    for r1, c1, r2, c2 in queries:
        total = ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]
        results.append(total)
    return results

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    queries = [[0, 0, 2, 2], [1, 0, 2, 1]]
    print(f"Query results: {calculate_2d_prefix_sum(matrix, queries)}")
