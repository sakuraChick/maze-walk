from maze_walk.algorithm.bfs import bfs
from maze_walk.algorithm.dfs import find_one_path
from maze_walk.factory import maze_factory
from maze_walk.model.maze import Maze
from maze_walk.utils import sort_routes


def process_maze(file_name: str):
    maze = maze_factory.from_file(file_name)
    maze.find_beginning()
    return maze

def solve(maze: Maze, x: int, y: int):
    path = find_one_path(maze, x, y)
    return sort_routes(path)[0]

def process_output(all_paths: list[list[tuple[int, int]]]):
    output = []
    for i, path in enumerate(all_paths):
        route = ''
        for point in path:
            route += f"{point} -> "
        route += "exit"

        output.append(f"Route {i+1}: {route}, length: {len(path)-1}\n") # the starting point does not count

    return "".join(output) if output != [] else "No available routes!"

def solve_maze_service(maze: Maze,
                       beginning: tuple[int, int] | None = None
                       ) -> str:
    if beginning is None:
        if maze.begin is not None:
            x_b, y_b = maze.begin
        else:
            raise ValueError("A starting point is required.")
    else:
        x_b, y_b = beginning

    if maze.is_wall(x_b, y_b):
        raise ValueError("The starting point is in the wall!")

    all_paths = solve(maze, x_b, y_b)

    return process_output(all_paths)