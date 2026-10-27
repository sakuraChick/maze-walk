import matplotlib.pyplot as plt

from maze_walk.model.maze import Maze
from maze_walk.plotter.maze_plotter import MazePlotter
from maze_walk.service.paths_solver_service import solve_maze_service


def main():
    print(solve_maze_service("test_maze_2.txt"))
    maze = Maze.from_file("test_maze_2.txt")
    static_plotter = MazePlotter.from_maze(maze)

    static_plotter.draw()
    plt.show()


if __name__ == '__main__':
    main()