import fileinput
import sys
from math import sqrt

TEST = False


def solve(line):
    numbers = list(map(lambda x: int(x), line.split()))
    return list(map(lambda x: str("%.4f" % sqrt(x)), numbers))


def main():
    data = fileinput.input()
    results_arr = []

    for i, line in enumerate(data):
        results_arr += solve(line)

    results_arr = [i for i in reversed(results_arr)]
    if TEST:
        for line, res in zip(open('output', 'r').readlines(), results_arr):
            print(line.split()[0] == res, line, res)
    else:
        result = '\n'.join(results_arr)
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
