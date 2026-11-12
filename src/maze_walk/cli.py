import argparse

from maze_walk.command.convert import run_convert
from maze_walk.command.search import run_search
from maze_walk.command.visualize import run_visualize


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Maze path finding and visualization"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Search module
    search_parser = commands.add_parser("search")

    search_parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="The maze in grid"
    )

    search_parser.add_argument(
        "-a", "--algorithm",
        choices=["dfs", "bfs"],
        required=True
    )

    search_parser.add_argument(
        "-b", "--begin",
        nargs=2,
        type=int,
        required=True
    )

    search_parser.set_defaults(func=run_search)

    # Visualization module
    visualize_parser = commands.add_parser("visualize")

    visualize_parser.add_argument(
        "-a", "--algorithm",
        choices=["dfs", "bfs", "static"],
        required=True,
        help="Algorithm type."
    )

    visualize_parser.add_argument(
        "-b", "--begin",
        nargs=2,
        type=int,
        required=True,
        help="The beginning point in x, y coordinates."
    )

    visualize_parser.add_argument(
        "-s", "--save",
        type=str,
        required=False,
        help="Key in the document name if you want to save the process as gif."
    )

    visualize_parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="The maze in grid."
    )

    visualize_parser.set_defaults(func=run_visualize)

    # Conversion module
    convert_parser = commands.add_parser("convert")

    convert_parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="The original file in bool values."
    )

    convert_parser.add_argument(
        "-c", "--col",
        required=True,
        type=int,
        help="How many columns does this maze have?"
    )

    convert_parser.add_argument(
        "-e", "--exit",
        required=True,
        nargs=2,
        type=int,
        help="Key in the coordinate of the exit if it does not exit in the maze (in the order of x and y)."
    )

    convert_parser.set_defaults(func=run_convert)

    return parser

def main():
    args = create_parser().parse_args()
    args.func(args)
