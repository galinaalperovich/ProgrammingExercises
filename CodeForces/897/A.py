import fileinput
import sys


# http://codeforces.com/contest/897/problem/0

class InputData:
    def __init__(self, ops, s):
        self.s = s
        self.ops = ops


class Result:
    def __init__(self, s):
        self.n = s

    def __str__(self):
        return '{}'.format(self.n)


def apply_operation(current_string, operation):
    l = operation[0]
    r = operation[1]
    c1 = operation[2]
    c2 = operation[3]
    sub_s = current_string[l - 1:r]
    new_str = current_string[:l - 1] + sub_s.replace(c1, c2) + current_string[r:]

    return new_str


def solve(input_data: InputData) -> Result:
    operations = input_data.ops
    current_string = input_data.s
    for operation in operations:
        current_string = apply_operation(current_string, operation)

    return Result(current_string)


def get_int_arr(line):
    l = [str(num) for num in line.replace('\n', '').split(' ')]
    l[0] = int(l[0])
    l[1] = int(l[1])
    return l


def main():
    input = fileinput.input(sys.argv[1:])

    n, m = get_int_arr(input.readline())
    s = input.readline().replace('\n', '')
    ops = []
    for i in range(m):
        operation = input.readline()
        ops.append(get_int_arr(operation))

    input_data = InputData(ops, s)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
