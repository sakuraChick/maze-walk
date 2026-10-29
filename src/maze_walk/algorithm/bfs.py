from collections import deque
from typing import Any

from maze_walk.model.maze import Maze


def bfs(maze: Maze, x: int, y: int) -> dict[tuple[int, int], list[Any]]:
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

    dist = {(x, y): 0}
    parents = {(x, y): []}
    q = deque([(x, y)])


    while q:
        x, y = q.popleft()
        if maze.is_exit(x, y):
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not maze.is_valid(nx, ny) or maze.is_wall(nx, ny):
                continue

            if (nx, ny) not in dist: # a new point
                dist[(nx, ny)] = dist[(x, y)] + 1
                parents[(nx, ny)] = [(x, y)]
                q.append((nx, ny))
            elif dist[(nx, ny)] == dist[(x, y)] + 1: # the point is also a child of (x, y) but not counted at first
                parents[(nx, ny)].append((x, y))

    return parents

def all_shortest_path(parents: dict[tuple[int, int], list[Any]], e: tuple[int, int], x: int, y: int):
    paths = []

    def build(cell, suffix):
        if cell == (x, y):
            paths.append([cell] + suffix)
            return
        for p in parents[cell]:
            build(p, [cell] + suffix)

    build(e, [])

    return paths


