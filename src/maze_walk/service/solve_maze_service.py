from maze_walk.algorithm.bfs import bfs
from maze_walk.algorithm.dfs import dfs
from maze_walk.model.maze import Maze


def solve(maze: Maze, algorithm_type: str, x: int, y: int):
    if algorithm_type == "dfs":
        return dfs(maze, x, y)
    elif algorithm_type == "bfs":
        return bfs(maze, x, y)
    else:
        raise ValueError("Please type in the correct algorithm")


def process_output(path: list[tuple[int, int]]) -> str:
    output = []
    route = ''
    for point in path:
        route += f"{point} -> "
    route += "exit"

    output.append(f"Route : {route}, length: {len(path)-1}\n") # the starting point does not count

    return "".join(output) if output != [] else "No available routes!"


def solve_maze_service(maze: Maze,
                       b_x: int,
                       b_y: int,
                       algorithm_type: str
                       ) -> str:
    maze.set_begin(b_x, b_y)

    if maze.is_wall(b_x, b_y):
        raise ValueError("The starting point is in the wall!")

    all_paths = solve(maze, algorithm_type, b_x, b_y)

    return process_output(all_paths)