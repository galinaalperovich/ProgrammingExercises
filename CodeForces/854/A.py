import fileinput
import sys


# http://codeforces.com/contest/854/problem/A

class InputData:
    def __init__(self, n):
        self.n = n


class Result:
    def __init__(self, a, b):
        self.b = b
        self.a = a

    def __str__(self):
        return '{} {}'.format(self.a, self.b)


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


# noinspection PyTypeChecker
def solve(input_data: InputData) -> Result:
    n = input_data.n

    a_last = (n - 1) // 2

    a_vals = list(range(1, a_last + 1))

    for a in a_vals[::-1]:
        b = n - a
        current_gcd = gcd(a, b)
        if current_gcd == 1:
            return Result(a, b)
        b += 1


def main():
    input = fileinput.input(sys.argv[1:])
    data_line = input.readline().replace('\n', '')
    n = int(data_line)

    input_data = InputData(n)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
