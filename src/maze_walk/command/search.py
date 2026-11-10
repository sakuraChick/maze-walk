from argparse import Namespace

from maze_walk.factory import maze_factory
from maze_walk.service.solve_maze_service import solve_maze_service


def run_search(args: Namespace) -> None:
    try:
        maze = maze_factory.from_file(args.file)
        print(solve_maze_service(maze, *args.begin, args.algorithm))
    except FileNotFoundError as e:
        print(f"Error! {e}")
