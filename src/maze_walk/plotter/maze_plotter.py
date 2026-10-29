from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

from maze_walk.model.maze import Maze


class MazePlotter:
    def __init__(self, maze: Maze):
        self._colormap = ListedColormap(
            ["white", # 0 for air
            "black", # 1 for wall
            "red", # 2 for exit
            "blue"] # 3 for starting point
        )
        self._color_grid = maze.get_grid()

    def draw_static(self):
        fig, ax = plt.subplots()
        im = ax.imshow(self._color_grid,
                  cmap=self._colormap,
                  interpolation="nearest")

        im.set_clim(-0.5, 3.5)

        ax.set_xticks([])
        ax.set_yticks([])

        return fig, ax, im