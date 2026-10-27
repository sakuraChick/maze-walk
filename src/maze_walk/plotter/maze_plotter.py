from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

from maze_walk.model.maze import Maze


class MazePlotter:
    def __init__(self, grid: npt.NDArray):
        self._colormap = ListedColormap(
            ["white", # 0 for air
            "black", # 1 for wall
            "red", # 2 for exit
            "blue"] # 3 for starting point
        )
        self._color_grid = grid

    def draw(self):
        fig, ax = plt.subplots()
        im = ax.imshow(self._color_grid,
                  cmap=self._colormap,
                  interpolation="nearest")

        ax.set_xticks([])
        ax.set_yticks([])

        return fig, ax, im

    @classmethod
    def from_maze(cls, maze: Maze):
        grid = np.zeros((maze.row, maze.col), dtype=np.int8)

        dict_to_val = {
            ' ': 0,
            '#': 1,
            'e': 2,
            'b': 3
        }

        for i, row in enumerate(maze):
            for j, char in enumerate(row):
                grid[i][j] = dict_to_val[maze.get_grid(j, i)]

        return cls(grid)