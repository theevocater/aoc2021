#!/usr/bin/env python3
import argparse
import re
from typing import List
from typing import Optional
from typing import Tuple


def print_floor(sea_floor: List[List[int]]) -> None:
    for row in sea_floor:
        print('\t'.join([str(i) for i in row]))


def parse_inputs(
        inputs: List[str],
) -> Tuple[int, List[Tuple[int, int, int, int]]]:
    matcher = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
    # create pairs, find max
    lines = []
    max_coord = 0
    for i in inputs:
        m = matcher.match(i)
        if m:
            a, b, x, y = m.groups()
            t = (int(a), int(b), int(x), int(y))
            if (local_max := max(t)) > max_coord:
                max_coord = local_max
            lines.append(t)
    return max_coord+1, lines


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input', nargs='?', default='input.txt',
        help='input file to read',
    )
    args = parser.parse_args()

    inputs = []
    with open(args.input) as f:
        inputs = [line.rstrip() for line in f]

    max_coord, lines = parse_inputs(inputs)

    # assume its a square grid
    sea_floor: List[List[int]] = [[]]*max_coord
    for i in range(max_coord):
        sea_floor[i] = [0]*max_coord
    print_floor(sea_floor)

    for a, b, x, y in lines:
        print(f'{a},{b} {x},{y}')
        if a == x:
            while b != y:
                sea_floor[a][b] += 1
                if b > y:
                    b -= 1
                else:
                    b += 1
            sea_floor[a][b] += 1
        elif b == y:
            while a != x:
                sea_floor[a][b] += 1
                if a > x:
                    a -= 1
                else:
                    a += 1
            sea_floor[a][b] += 1
        else:
            print('ignoring diagonal')
    print()
    print_floor(sea_floor)
    above_two = 0
    for row in sea_floor:
        for point in row:
            if point >= 2:
                above_two += 1
    print(f'crosses: {above_two}')

    return 0


if __name__ == '__main__':
    exit(main())
