import matplotlib.pyplot as plt

from maze_walk.algorithm.dfs import find_one_path
from maze_walk.algorithm.dfs_speed_test import dfs_speed_test
from maze_walk.factory import maze_factory
from maze_walk.plotter.maze_animator import MazeAnimator
from maze_walk.plotter.maze_plotter import MazePlotter
from maze_walk.service.paths_solver_service import solve_maze_service


def main():
    maze = maze_factory.from_bool("maze.txt", 51, (1, 47), (46, 1))
    path, events = find_one_path(maze, 46, 1) # 1697620
    print(path)
    animator = MazeAnimator(maze, events)
    animator.run()
    plt.show()


if __name__ == '__main__':
    main()