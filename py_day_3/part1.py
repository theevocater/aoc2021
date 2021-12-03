#!/usr/bin/env python3
import argparse
from typing import Dict
from typing import List
from typing import Optional


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

    bit_rate: Dict[int, Dict[str, int]] = {}
    for line in inputs:
        for i, a in enumerate(line):
            pos = bit_rate.get(i, {})
            if a in pos:
                pos[a] += 1
            else:
                pos[a] = 1
            bit_rate[i] = pos

    print(bit_rate)

    gamma_bits = ['']*len(bit_rate)
    for position, values in bit_rate.items():
        m = max(values.items(), key=lambda x: x[1])
        gamma_bits[position] = m[0]

    gamma = int(''.join(gamma_bits), base=2)
    epsilon = 2**len(gamma_bits) - gamma - 1
    print(f'{gamma} * {epsilon} = {gamma * epsilon}')

    return 0


if __name__ == '__main__':
    exit(main())
