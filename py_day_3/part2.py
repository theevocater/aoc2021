#!/usr/bin/env python3
import argparse
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

    bit_pos = 0
    common_bits = ''
    filtered_inputs = inputs.copy()
    # iterate through the columns first
    for i in range(len(inputs[0])):
        zeros = 0
        ones = 0
        if len(filtered_inputs) == 1:
            break
        for line in filtered_inputs:
            print(f'{common_bits} {line}')
            bit = line[bit_pos]
            if bit == '0':
                zeros += 1
            if bit == '1':
                ones += 1

        print(f'{zeros} {ones}')
        bit_pos += 1
        if zeros > ones:
            common_bits += '0'
        else:
            common_bits += '1'
        filtered_inputs = [
            fi
            for fi in filtered_inputs
            if fi.startswith(common_bits)
        ]

    oxygen = int(filtered_inputs[0], base=2)

    bit_pos = 0
    common_bits = ''
    filtered_inputs = inputs.copy()
    # iterate through the columns first
    for i in range(len(inputs[0])):
        zeros = 0
        ones = 0
        if len(filtered_inputs) == 1:
            break
        for line in filtered_inputs:
            print(f'{common_bits} {line}')
            bit = line[bit_pos]
            if bit == '0':
                zeros += 1
            if bit == '1':
                ones += 1

        print(f'{zeros} {ones}')
        bit_pos += 1
        if zeros <= ones:
            common_bits += '0'
        else:
            common_bits += '1'
        filtered_inputs = [
            fi
            for fi in filtered_inputs
            if fi.startswith(common_bits)
        ]

    c02 = int(filtered_inputs[0], base=2)

    print(f'{oxygen} {c02} = {oxygen*c02}')

    return 0


if __name__ == '__main__':
    exit(main())
