import argparse

parser = argparse.ArgumentParser(
    description="test parser"
)

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

algorithm_parser = subparsers.add_parser("calculate")

algorithm_parser.add_argument(
    "-a", "--algorithm",
)

args = parser.parse_args()

print(args.algorithm, args.command)