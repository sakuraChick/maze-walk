from typing import NamedTuple, Any

from maze_walk.model.maze import Maze

class DfsEvent(NamedTuple):
    type: str
    point: tuple[int, int]
    path: list[tuple[int, int]]


def _dfs(maze: Maze, x: int, y: int, cur_path: list[tuple[int, int]], visited: list[tuple[int, int]]):
    if not maze.is_valid(x, y):
        return

    if (x, y) in visited:
        return
    else:
        visited.append((x, y))

    if (x, y) in cur_path: # going back (which means this is a dead end or a loop)
        return

    cur_path.append((x, y))
    yield DfsEvent("entering", (x, y), cur_path.copy())

    if maze.is_exit(x, y):
        yield DfsEvent('found', (x, y), cur_path.copy())

        cur_path.pop() # going back for one step and search for other possible paths
        yield DfsEvent('backtracking', (x, y), cur_path.copy())

        return

    if maze.is_wall(x, y):
        cur_path.pop()
        yield DfsEvent('backtracking', (x, y), cur_path.copy())
        return # a path through wall is not valid

    # iterate through four directions and recursively update all possible paths
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        yield from _dfs(maze, x + dx, y + dy, cur_path, visited)

    cur_path.pop() # remove this point and go back one step since all the directions have been explored
    yield DfsEvent("backtracking", (x, y), cur_path.copy())


def dfs(maze, x, y):
    """
    Receive a maze and the coordinate of a valid starting point, use DFS search to find out one path.
    :param maze: the maze in grid form
    :param x: x coordinate of the starting point
    :param y: y coordinate of the starting point
    :return: raw path in list, and all `DfsEvents` generated
    """
    path = []
    visited = []
    events = []

    for event in _dfs(maze, x, y, path, visited):
        events.append(event)

        if event.type == "found":
            break

    return path, events
