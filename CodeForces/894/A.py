import fileinput
import sys


# http://codeforces.com/contest/894/problem/0

class InputData:
    def __init__(self, line):
        self.line = line


class Result:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return '{}'.format(self.n)


def solve(input_data: InputData) -> Result:
    line = input_data.line
    c_start = 0
    c_middle = 0
    c_end = 0
    for w in line:
        if w == 'Q':
            c_start += 1
            c_end += c_middle
        elif w == 'A':
            c_middle += c_start

    return Result(c_end)


def main():
    input = fileinput.input(sys.argv[1:])
    data_line = input.readline().replace('\n', '')
    input_data = InputData(data_line)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
