from pathlib import Path
import numpy as np

from maze_walk.model.maze import Maze


def from_file(file_name: str) -> Maze:
    """
    :param file_name: load a file from ./src/assets/grid/file_name
    :return: the maze
    """
    file_path = Path(__file__).resolve().parents[3] / 'assets' / 'grid' / file_name
    with open(file_path, "r") as f:
        lines = [line.strip().split() for line in f.readlines()]

    grid = np.array(lines, dtype=np.int8)
    return Maze(grid)


def from_bool(file_name: str, cols: int, e: tuple[int, int] | None = None) -> Maze:
    """
    THe file should be made up of rows * columns of boolean values, where
    - True: stands for Wall
    - False: stands for air

    Note that no exit or beginning point should be given in the file
    :param cols: total number of columns
    :param e: the (x, y) coordinate of the exit
    :param file_name: file name
    :return: the maze
    """
    file_path = Path(__file__).resolve().parents[3] / "assets" / "maze" / file_name
    with open(file_path, "r") as f:
        bool_lines = [eval(line.strip()) for line in f.readlines()]

    rows = len(bool_lines) // cols
    maze_lines = np.zeros((rows, cols), dtype=np.int8)

    for cur_col in range(cols):
        for cur_row in range(rows):
            if bool_lines[cur_col * rows + cur_row]:
                maze_lines[cur_row, cur_col] = 1
            else:
                maze_lines[cur_row, cur_col] = 0

    maze = Maze(maze_lines)

    if e is not None:
        maze.set_exit(*e)

    return maze