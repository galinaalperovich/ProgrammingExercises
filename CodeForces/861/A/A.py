import fileinput

import sys

# http://codeforces.com/contest/861/problem/A

a = None
k = None
result = None


def gcd(a, b):
    return abs(a) if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def solve():
    global k, a, result

    b = 10 ** k

    if b == 0 or a % b == 0:
        result = str(a)
    else:
        result = str(lcm(a, b))


def main():
    input = fileinput.input(sys.argv[1:])
    data_line = input.readline().replace('\n', '')

    global a, k
    input_line = data_line.split()
    a = int(input_line[0])
    k = int(input_line[1])

    solve()

    global result

    sys.stdout.write(result)


if __name__ == '__main__':
    main()
