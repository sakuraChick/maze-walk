import time

from maze_walk.model.maze import Maze


def dfs_speed_test(maze, sx, sy, time_lim: int):
    start = time.time()
    count = 0

    def dfs(x: int, y: int, all_paths: list[list[tuple[int, int]]], cur_path: list[tuple[int, int]]):
        nonlocal count

        if time.time() - time_lim > start:
            return

        if not maze.is_valid(x, y):
            return

        if (x, y) in cur_path: # going back (which means this is a dead end or a loop)
            return

        cur_path.append((x, y))
        count += 1

        if maze.is_exit(x, y):
            all_paths.append(cur_path.copy()) # this is a valid path!
            cur_path.pop() # going back for one step and search for other possible paths
            return

        if maze.is_wall(x, y):
            cur_path.pop()
            return # a path through wall is not valid

        # iterate through four directions and recursively update all possible paths
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(x + dx, y + dy, all_paths, cur_path,)

        cur_path.pop() # remove this point and go back one step since all the directions have been explored

    dfs(sx, sy, [], [])
    return count