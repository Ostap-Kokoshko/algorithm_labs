def ijones(matrix, height, width):
    sub_path = [[0 for _ in range(width)] for _ in range(height)]
    alphabet = {}

    for curr_height in range(height):
        sub_path[curr_height][0] = 1
        if matrix[curr_height][0] not in alphabet:
            alphabet[matrix[curr_height][0]] = 0
        alphabet[matrix[curr_height][0]] += 1

    for curr_width in range(1, width):
        sub_alphabet = {}
        for curr_height in range(height):
            sub_path[curr_height][curr_width] = alphabet.get(matrix[curr_height][curr_width], 0)
            if matrix[curr_height][curr_width] != matrix[curr_height][curr_width - 1]:
                sub_path[curr_height][curr_width] += sub_path[curr_height][curr_width - 1]

            if matrix[curr_height][curr_width] not in sub_alphabet:
                sub_alphabet[matrix[curr_height][curr_width]] = 0
            sub_alphabet[matrix[curr_height][curr_width]] += sub_path[curr_height][curr_width]

        for key, val in sub_alphabet.items():
            if key not in alphabet:
                alphabet[key] = val
            else:
                alphabet[key] += val

    if height == 1:
        result = sub_path[0][width - 1]
    else:
        result = sub_path[0][width - 1] + sub_path[height - 1][width - 1]

    return result


def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    matrix_width, matrix_height = map(int, lines[0].split())
    matrix = [list(line.strip()) for line in lines[1:]]

    return matrix_height, matrix_width, matrix


def write_result_to_file(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


if __name__ == "__main__":
    height, width, matrix = read_matrix_from_file("ijones_in.txt")
    result = ijones(matrix, height, width)
    write_result_to_file("ijones_out.txt", result)
