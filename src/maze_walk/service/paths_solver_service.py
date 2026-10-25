from maze_walk.algorithm.dfs import find_all_paths
from maze_walk.model.maze import Maze
from maze_walk.utils import sort_routes


def process_maze(file_name: str):
    maze = Maze.from_file(file_name)
    maze.find_beginning()
    return maze

def solve_from_given_beginning(maze: Maze):
    all_paths = find_all_paths(maze, maze.x_b, maze.y_b)
    return sort_routes(all_paths)

def solve_from_xy(maze: Maze, x: int, y: int):
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

def solve_maze_service(file_name: str):
    maze = process_maze(file_name)

    if maze.x_b is not None and maze.y_b is not None:
        all_paths = solve_from_given_beginning(maze)
    else:
        x_b, y_b = eval(input("The selected coordinate is a wall, please enter x, y coordinate of the beginning point (with a comma): "))
        while maze.is_wall(x_b, y_b):
           x_b, y_b = eval(input("Please enter a valid coordinate: "))
        all_paths = solve_from_xy(maze, x_b, y_b)

    print(process_output(all_paths))
