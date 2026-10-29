from typing import Any

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap

from maze_walk.model.maze import Maze


class MazeAnimator:
    def __init__(self, maze: Maze, events: list[Any]):
        self.ani = None
        self.maze_state = maze.get_grid()
        self.INIT_MAZE = maze.get_grid()
        self._colormap = ListedColormap(
            ["white",  # 0 for air
             "black",  # 1 for wall
             "red",  # 2 for exit
             "blue", # 3 for starting point
             "green",  # 4 for current path
            "yellow", # 5 head
             "grey"] # 6 visited
        )

        self.events = events

        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.maze_state,
                  cmap=self._colormap,
                  interpolation="nearest")

        self.im.set_clim(-0.5, 6.5)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.title = self.ax.set_title("Maze Search")

    def init(self):
        self.im.set_data(self.INIT_MAZE)
        self.title.set_text("Maze Search: Initializing...")

        return self.im, self.title

    def update(self, frame):
        event_type, cur_point, cur_path = self.events[frame]

        cur_x, cur_y = cur_point
        if event_type == "backtracking" and self.INIT_MAZE[cur_y, cur_x] != 1:
            self.maze_state[cur_y, cur_x] = 0
        elif self.INIT_MAZE[cur_y, cur_x] == 0:
            self.maze_state[cur_y, cur_x] = 5

        for path_x, path_y, in cur_path:
            if self.INIT_MAZE[cur_y, cur_x] == 0:
                self.maze_state[path_y, path_x] = 4

        self.im.set_data(self.maze_state)

        self.title.set_text(f"Maze Search: Step {frame+1}, {event_type}")

        return self.im, self.title

    def run(self):
        self.ani = animation.FuncAnimation(
            fig=self.fig,
            func=self.update,
            init_func=self.init,
            frames=len(self.events),
            interval=10,
            blit=False,
            repeat=False
        )


