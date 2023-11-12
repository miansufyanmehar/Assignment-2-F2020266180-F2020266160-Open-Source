import argparse
import json

from board import Board

board = Board()


def main(arguments):
    with open(arguments.infile, "r") as infile:
        input_instructions = infile.readlines()
        for line in input_instructions:
            if line.find(":") > 0:
                _line = line.replace("\n", '')
                knight, direction = _line.split(":")
                board.read_input(knight, direction)
    with open(arguments.outfile, "w") as outfile:
        json.dump(board.output(), outfile, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='input/moves.txt',
                        help='input/moves.txt')
    parser.add_argument('--outfile', type=str, default="output/final_state.json",
                        help='output/final_state.json')
    args = parser.parse_args()
    main(arguments=args)
