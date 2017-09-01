import sys


def solve(line):
    kxy = list(map(lambda x: int(x), line.split(' ')))
    k = kxy[0]
    x = kxy[1]
    y = kxy[2]
    r = 0
    if x == y:
        if x >= k:
            r = 2
        else:
            dif_kx = k - x
            if dif_kx in [0, 1]:
                r = 2
            else:
                r = dif_kx
    elif x > y:
        dif_xy = x - y
        dif_kx = k - x
        if dif_kx < 0:
            if dif_xy == 2:
                r = 0
            else:
                r = 1
        elif dif_kx == 0 and dif_xy == 1:
            r = 1
        else:
            r = dif_kx
    else:
        dif_ky = k - y
        dif_xy = y - x
        if dif_ky < 0:
            if dif_xy == 2:
                r = 0
            else:
                r = 1
        elif dif_ky == 0 and dif_xy == 1:
            r = 1
        else:
            r = dif_ky

    return r


def main():
    data = sys.stdin.readlines()
    lines_arr = []
    results_arr = []

    for i, line in enumerate(data):
        if i == 0:
            continue
        results_arr.append(str(solve(line)))
        lines_arr.append(line)

    # result = '\n'.join(list(map(str, zip(lines_arr, results_arr))))
    result = '\n'.join(results_arr)
    sys.stdout.write(result)


if __name__ == '__main__':
    main()
