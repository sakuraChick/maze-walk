import matplotlib.pyplot as plt

from src.maze_walk.service.path_visualization_service import (
    PROJECT_ROOT,
    load_maze,
    find_exits,
    with_exit,
    validate_point,
    collect_search,
    save_routes,
)
from src.maze_walk.plottor.maze_plot import animate_search


INTERVAL_MS = 10
FIXED_EXIT = None


def main():
    file_name = input("Maze file: ").strip()
    maze = load_maze(file_name)

    if FIXED_EXIT is not None:
        maze = with_exit(maze, FIXED_EXIT)

    exits = find_exits(maze)

    print(f"x: 0 to {maze.col - 1}, y: 0 to {maze.row - 1}")
    start = tuple(map(int, input("Start x,y: ").split(",")))
    validate_point(maze, start)

    paths, frames = collect_search(maze, start, INTERVAL_MS)

    output = PROJECT_ROOT / "output"
    output.mkdir(exist_ok=True)

    save_routes(paths[:1], start, exits, output / "shortest_route.txt")

    if paths:
        print(f"Shortest route: {len(paths[0]) - 1} steps")

    save_gif = input("Save GIF? y/n: ").strip().lower()
    gif_path = output / "maze_search.gif" if save_gif == "y" else None

    animation = animate_search(
        maze,
        start,
        frames,
        interval=INTERVAL_MS,
        gif_path=gif_path,
    )

    plt.show()
    return animation


if __name__ == "__main__":
    main()