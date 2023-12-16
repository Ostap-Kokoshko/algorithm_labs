def matrix(n, m):
    start_matrix = []
    number = 1
    for rows in range(n):
        row = []
        for columns in range(m):
            row.append(number)
            number += 1
        start_matrix.append(row)
    return start_matrix


def zigzag_traversal(input_matrix):
    n = len(input_matrix)
    m = len(input_matrix[0])
    final_array = [[] for _ in range(m + n - 1)]

    for rows in range(n):
        for columns in range(m):
            position_element = rows + columns
            if position_element % 2 == 0:
                final_array[position_element].insert(0, input_matrix[rows][columns])
            else:
                final_array[position_element].append(input_matrix[rows][columns])

    result = []
    for sublist in final_array:
        result.extend(sublist)

    return result
