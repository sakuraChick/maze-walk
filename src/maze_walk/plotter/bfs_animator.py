from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap

from maze_walk.algorithm.dfs import DfsEvent
from maze_walk.model.maze import Maze


class BfsAnimator:
    def __init__(self, maze: Maze):
        self.ani: animation.FuncAnimation | None = None
        self.INIT_MAZE = maze.get_grid().copy()
        self.maze_state = self.INIT_MAZE.copy()
        self._colormap = ListedColormap(
            ["white",  # 0 for air
             "black",  # 1 for wall
             "red",  # 2 for exit
             "blue",  # 3 for starting point
             "green",  # 4 for built path
             "yellow"]  # 5 for temp path
        )

        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(self.maze_state,
                                 cmap=self._colormap,
                                 interpolation="nearest")

        self.im.set_clim(-0.5, 5.5)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.title = self.ax.set_title("Maze BFS Search")

    def init(self):
        self.maze_state = self.INIT_MAZE.copy()
        self.im.set_data(self.maze_state)
        self.title.set_text("Maze BFS Search: Initializing...")

        return self.im, self.title

    def update(self, frame, events: list[DfsEvent]):
        cur_event = events[frame]

        cur_x, cur_y = cur_event.point
        is_special = self.INIT_MAZE[cur_y, cur_x] != 1 and self.INIT_MAZE[cur_y, cur_x] != 2 and self.INIT_MAZE[cur_y, cur_x] != 3
        if cur_event.type == "discovered" and is_special:
            self.maze_state[cur_y, cur_x] = 5
        elif cur_event.type == "building" or cur_event.type == "found" and is_special:
            self.maze_state[cur_y, cur_x] = 4

        self.im.set_data(self.maze_state)
        self.title.set_text(f"Maze BFS Search: Step {frame+1}, {cur_event.type}")

        return self.im, self.title

    def run(self, events: tuple[Any]):
        self.ani = animation.FuncAnimation(
            fig=self.fig,
            func=self.update,
            fargs=(events,),
            init_func=self.init,
            frames=len(events),
            interval=50,
            blit=False,
            repeat=False
        )

    def save(self, file_name: str):
        file_path = Path(__file__).resolve().parents[3] / "assets" / "image" / file_name
        file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.ani is not None:
            self.ani.save(file_path, writer="pillow")
        else:
            raise RuntimeError("Run the BFS animation before saving it.")
