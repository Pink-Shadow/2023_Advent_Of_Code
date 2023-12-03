
def is_part_num(matrix, row, col):
    for i in range(-1, 2):
        if (not matrix[row-1][col+i].isdigit()) and matrix[row-1][col+i] != ".":
            return True

    for i in range(-1, 2):
        if (not matrix[row+1][col+i].isdigit()) and matrix[row+1][col+i] != ".":
            return True

    if (not matrix[row][col+1].isdigit()) and matrix[row][col+1] != ".":
        return True

    if (not matrix[row][col-1].isdigit()) and matrix[row][col-1] != ".":
        return True

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as infile:
        content = infile.readlines()
        matrix = [x.strip() for x in content]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col].isdigit():
                    # print(matrix[row][col])

                    if is_part_num(matrix, row, col):
                        print(matrix[row][col])




