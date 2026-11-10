from collections import deque
from typing import Any, NamedTuple, Iterator

from maze_walk.model.maze import Maze

class BfsEvent(NamedTuple):
    type: str
    point: tuple[int, int]
    parent: tuple[int, int] | None = None
    dist: int | None = None


def _bfs(maze: Maze, x: int, y: int, parent: dict[tuple[int, int], tuple[int, int]]) -> Iterator[BfsEvent]:
    dist = {(x, y): 0}
    visited = []
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        else:
            visited.append((x, y))

        if maze.is_exit(x, y):
            yield BfsEvent("found", (x, y), parent=parent[(x, y)], dist=dist[(x, y)])
            continue

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy

            if not maze.is_valid(nx, ny) or maze.is_wall(nx, ny):
                continue
            if (nx, ny) in parent:
                continue

            if (nx, ny) not in dist: # a new point
                dist[(nx, ny)] = dist[(x, y)] + 1
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))

            yield BfsEvent("discovered", (nx, ny), (x, y), dist[(nx, ny)])

    yield BfsEvent("finished", (x, y))


def build(end: tuple[int, int], parent: dict[tuple[int, int], tuple[int, int]], path: list[tuple[int, int]]) -> Iterator[BfsEvent]:
    dummy = end
    while parent.get(dummy):
        dummy = parent[dummy]
        path.append(dummy)
        yield BfsEvent("building", dummy)

    path.reverse()


def bfs(maze: Maze, x: int, y: int):
    """
    Receive a maze and the coordinate of a valid starting point, use BFS search to find out the shortest path.
    :param maze: the maze in grid form
    :param x: x coordinate of the starting point
    :param y: y coordinate of the starting point
    :return: raw path in list, and all `BfsEvents` generated
    """
    path = []
    events = []
    parent = {}
    end = (-1, -1)

    for event in _bfs(maze, x, y, parent):
        events.append(event)

        if event.type == "found":
            end = event.point
            break

    for event in build(end, parent, path):
        events.append(event)

    return path, events

