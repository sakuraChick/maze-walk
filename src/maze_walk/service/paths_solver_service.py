from maze_walk.algorithm.dfs import find_all_paths
from maze_walk.model.maze import Maze
from maze_walk.utils import sort_routes


def process_maze(file_name: str):
    maze = Maze.from_file(file_name)
    maze.find_beginning()
    return maze

def solve(maze: Maze, x: int, y: int):
    all_paths = find_all_paths(maze, x, y)
    return sort_routes(all_paths)

def process_output(all_paths: list[list[tuple[int, int]]]):
    output = []
    for i, path in enumerate(all_paths):
        route = ''
        for point in path:
            route += f"{point} -> "
        route += "exit"

        output.append(f"Route {i+1}: {route}, length: {len(path)}\n")

    return "".join(output) if output != [] else "No available routes!"

def solve_maze_service(file_name: str,
                       beginning: tuple[int, int] | None = None
                       ) -> str:
    maze = process_maze(file_name)

    if beginning is None:
        if maze.x_b is not None and maze.y_b is not None:
            x_b, y_b = maze.x_b, maze.y_b
        else:
            raise ValueError("A starting point is required.")
    else:
        x_b, y_b = beginning

    if maze.is_wall(x_b, y_b):
        raise ValueError("The starting point is in the wall!")

    all_paths = solve(maze, x_b, y_b)

    return process_output(all_paths)