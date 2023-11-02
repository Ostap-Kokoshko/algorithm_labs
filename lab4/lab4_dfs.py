def flood_fill(matrix, x, y, currColor, newColor):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != currColor:
        return

    matrix[x][y] = newColor
    flood_fill(matrix, x + 1, y, currColor, newColor)
    flood_fill(matrix, x - 1, y, currColor, newColor)
    flood_fill(matrix, x, y + 1, currColor, newColor)
    flood_fill(matrix, x, y - 1, currColor, newColor)


matrix2 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1],
]

x = 0
y = 0

prevC = matrix2[x][y]

newC = 3

flood_fill(matrix2, x, y, prevC, newC)

for i in range(len(matrix2)):
    for j in range(len(matrix2[0])):
        print(matrix2[i][j], end=' ')
    print()
