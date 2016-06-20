# env/bin/python3
# Kuskova Natalia

count = 0


def pyramid(triangle, row=0, col=0, sum_=0):
    global count
    count += 1
    if row == len(triangle) - 1:
        return sum_ + triangle[row][col]
    return max(pyramid(triangle, row + 1, col, sum_ + triangle[row][col]),
               pyramid(triangle, row + 1, col + 1, sum_ + triangle[row][col]))


if __name__ == "__main__":
    pyramid1 = [
                [7],
                [2, 3],
                [3, 3, 1],
                [3, 1, 5, 4],
                [3, 1, 3, 1, 3],
                [2, 2, 2, 2, 2, 2],
                [5, 6, 4, 5, 6, 4, 3]
                ]
    pyramid2 = [
                [1],
                [2, 1],
                [1, 2, 1],
                [1, 2, 1, 1],
                [1, 2, 1, 1, 1],
                [1, 2, 1, 1, 1, 1],
                [1, 2, 1, 1, 1, 1, 9]
                ]
    print("Pyramid 1: " + str(pyramid(pyramid1)))
    print("Pyramid 2: " + str(pyramid(pyramid2)))
