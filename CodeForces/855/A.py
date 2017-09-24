import fileinput
import sys


# http://codeforces.com/contest/855/problem/A

class InputData:
    def __init__(self, n, names):
        self.names = names
        self.n = n


class Result:
    def __init__(self, names_result):
        self.names_result = names_result

    def __str__(self):
        return '\n'.join(self.names_result)


def solve(input_data: InputData) -> Result:
    names = input_data.names
    names_set = set()
    names_result = []
    for name in names:
        if name in names_set:
            names_result.append('YES')
        else:
            names_result.append('NO')
            names_set.add(name)

    return Result(names_result)


def main():
    input = fileinput.input(sys.argv[1:])
    names = []
    n = int(input.readline())
    for i in range(n):
        names.append(input.readline().replace('\n', ''))

    input_data = InputData(n, names)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
