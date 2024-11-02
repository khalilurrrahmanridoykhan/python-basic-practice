def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def is_within_bounds(i, j):
        return 0 <= i < n and 0 <= j < m

    dominant_count = 0

    for i in range(n):
        for j in range(m):
            current_value = grid[i][j]
            is_dominant = True

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if is_within_bounds(ni, nj) and grid[ni][nj] >= current_value:
                    is_dominant = False
                    break

            if is_dominant:
                dominant_count += 1

    return dominant_count

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    result = numCells(grid)
    print(result)
