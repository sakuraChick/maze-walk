from maze_walk.algorithm.bfs import bfs
from maze_walk.algorithm.dfs import dfs
from maze_walk.model.maze import Maze
from maze_walk.plotter.bfs_animator import BfsAnimator
from maze_walk.plotter.dfs_animator import DfsAnimator
from maze_walk.plotter.maze_plotter import MazePlotter
from maze_walk.service.solve_maze_service import process_output


class VisualizationService:
    def __init__(self):
        self._active_objects: list[object] = []
        self._handlers = {
            "dfs": self._run_dfs,
            "bfs": self._run_bfs,
            "static": self._draw_static,
        }

    def execute(self, maze: Maze, x: int, y: int, type_: str, file_name: str | None = None) -> str:
        maze.set_begin(x, y)
        try:
            handler = self._handlers[type_]
        except KeyError:
            raise ValueError(f"Unsupported visualization type: {type_}") from None
        path = handler(maze, x, y, file_name)

        return process_output(path)

    def _run_dfs(self, maze: Maze, x: int, y: int, file_name: str | None) -> list[tuple[int, int]]:
        path, events = dfs(maze, x, y)
        animator = DfsAnimator(maze)
        self._active_objects.append(animator)
        animator.run(events)
        if file_name is not None:
            animator.save(file_name)
        return path

    def _run_bfs(self, maze: Maze, x: int, y: int, file_name: str | None) -> list[tuple[int, int]]:
        path, events = bfs(maze, x, y)
        animator = BfsAnimator(maze)
        self._active_objects.append(animator)
        animator.run(events)
        if file_name is not None:
            animator.save(file_name)
        return path

    def _draw_static(self, maze: Maze, x: int, y: int, file_name: str | None) -> list[tuple[int, int]]:
        if file_name is not None:
            raise ValueError("Saving is only supported for dfs and bfs animations.")
        MazePlotter(maze).draw_static()
        return []
