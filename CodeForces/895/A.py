import fileinput
import sys


# http://codeforces.com/contest/895/problem/0

class InputData:
    def __init__(self, n, angles):
        self.angles = angles
        self.n = n


class Result:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return '{}'.format(self.n)


def get_ss(i, j, angles):
    s1_arr = angles[i:j]
    s2_arr = angles[:i] + angles[j:]
    s1 = sum(s1_arr)
    s2 = sum(s2_arr)
    return s1, s2


def solve(input_data: InputData) -> Result:
    angles = input_data.angles
    results = []
    for i, a_i in enumerate(angles):
        for j, a_j in enumerate(angles):
            if i <= j:
                s1, s2 = get_ss(i, j, angles)
                results.append(abs(s1 - s2))

    return Result(min(results))


def main():
    input = fileinput.input(sys.argv[1:])
    n = input.readline().replace('\n', '')
    angles = [int(angle) for angle in input.readline().replace('\n', '').split(' ')]
    input_data = InputData(n, angles)
    result = solve(input_data)

    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()
