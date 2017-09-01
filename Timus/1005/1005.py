import fileinput
import sys

TEST = False


def solve(n, ws):
    A = []
    B = []
    for n in sorted(ws, reverse=True):
        if sum(A) < sum(B):
            A.append(n)
        else:
            B.append(n)

    return str(abs(sum(A) - sum(B)))


def main():
    data = fileinput.input()
    result = None
    n = None
    ws = None

    for i, line in enumerate(data):
        if i == 0:
            n = int(line.strip())
        else:
            ws = list(map(int, line.strip().split()))

    result = solve(n, ws)

    if TEST:
        for line, res in zip(open('output', 'r').readlines(), result):
            print(line.split()[0] == res, line, res)
    else:
        sys.stdout.write(result)


if __name__ == '__main__':
    main()
