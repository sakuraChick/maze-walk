import matplotlib.pyplot as plt

from maze_walk.algorithm.dfs_speed_test import dfs_speed_test
from maze_walk.factory import maze_factory
from maze_walk.plotter.maze_plotter import MazePlotter
from maze_walk.service.paths_solver_service import solve_maze_service


def main():
    maze = maze_factory.from_bool("maze.txt", 51, (47, 1), (1, 46))
    print(dfs_speed_test(maze, 1, 46, 5)) # 1697620

    plt.show()


if __name__ == '__main__':
    main()