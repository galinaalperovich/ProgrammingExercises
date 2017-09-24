import fileinput
import sys


# http://codeforces.com/problemset/problem/754/B

class InputData:
    def __init__(self, matrix):
        self.matrix = matrix


class Result:
    def __init__(self, result):
        self.result = result

    def __str__(self):
        return str(self.result)


def get_str_to_check(str_arr):
    result = str_arr[:]

    word = ''
    for i in range(4):
        for s in str_arr:
            word += s[i]

        result += [word]
        word = ''

    diag_word_1 = ''
    diag_word_2 = ''
    for i in range(4):
        diag_word_1 += str_arr[i][i]
        diag_word_2 += str_arr[i][-i - 1]

    result.append(diag_word_1)
    result.append(diag_word_2)

    diag_word_1 = ''
    diag_word_2 = ''
    diag_word_3 = ''
    diag_word_4 = ''
    for i in range(3):
        diag_word_1 += str_arr[i][i + 1]
        diag_word_2 += str_arr[i + 1][i]
        diag_word_3 += str_arr[i][-i - 2]
        diag_word_4 += str_arr[i + 1][-i - 1]

    result.append(diag_word_1)
    result.append(diag_word_2)
    result.append(diag_word_3)
    result.append(diag_word_4)

    return result


def solve(input_data: InputData) -> Result:
    str_arr = input_data.matrix
    full_str_arr = get_str_to_check(str_arr)
    correct_patterns = ['x.x', 'xx.', '.xx']
    for s in full_str_arr:
        for pattern in correct_patterns:
            if pattern in s:
                return Result('YES')

    return Result('NO')


def main():
    str_arr = []

    input_stream = fileinput.input(sys.argv[1:])

    for i in range(4):
        str_arr.append(input_stream.readline().replace('\n', ''))

    input_data = InputData(str_arr)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
