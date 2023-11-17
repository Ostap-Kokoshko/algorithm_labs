def floodfill_bfs(matrix, row, col, height, width, new_color, old_color):
    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        if row < 0 or col < 0 or row >= height or col >= width or matrix[row][col] != old_color:
            continue

        matrix[row][col] = new_color
        queue.append((row + 1, col))
        queue.append((row - 1, col))
        queue.append((row, col + 1))
        queue.append((row, col - 1))


with open('input_matrix.txt', 'r', encoding="utf-8") as file:
    height, width = [int(x) for x in file.readline().strip().split(",")]
    x, y = [int(x) for x in file.readline().strip().split(",")]
    new_color = file.readline().strip().replace("'", '')
    matrix = []
    for _ in range(height):
        row = file.readline().strip()
        row = [text.strip()[1:-1] for text in row.replace('[', '').replace('],', '').replace(']', '').split(',')]
        matrix.append(row)

prevC = matrix[x][y]
floodfill_bfs(matrix, x, y, height, width, new_color, prevC)

with open('output_matrix.txt', 'w', encoding="utf-8") as file:
    for row in matrix:
        file.write(' '.join(row) + '\n')

print(f"x = {x}, y = {y}, height = {height}, width = {width}, new color = {new_color}")
print("----------------------------------------------")

for row in matrix:
    print(' '.join(row))
