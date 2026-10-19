from src.maze_walk.model.maze import Maze


def dfs(maze: Maze, x: int, y: int, all_paths: list[list[tuple[int, int]]], cur_path: list[tuple[int, int]]):
    """
    The core method of
    :param maze: a 2 * 2 array, reflecting the types (such as wall, air, exit) in each grid
    :param x: x coordinate of current starting point
    :param y: y coordinate of current starting point
    :param all_paths: all the possible paths to the exit so far
    :param cur_path: current path (building)
    :return:
    """
    if not maze.is_valid(x, y):
        return

    if (x, y) in cur_path: # going back (which means this is a dead end or a loop)
        return

    cur_path.append((x, y))
    yield "enter", (x, y), cur_path.copy()

    if maze.is_exit(x, y):
        all_paths.append(cur_path.copy()) # this is a valid path!
        yield 'found', (x, y), cur_path.copy()

        cur_path.pop() # going back for one step and search for other possible paths
        yield 'backtrack', (x, y), cur_path.copy()

        return

    if maze.is_wall(x, y):
        cur_path.pop()
        yield 'backtrack', (x, y), cur_path.copy()
        return # a path through wall is not valid

    # iterate through four directions and recursively update all possible paths
    dfs(maze, x, y + 1, all_paths, cur_path)
    dfs(maze, x, y - 1, all_paths, cur_path)
    dfs(maze, x + 1, y, all_paths, cur_path)
    dfs(maze, x - 1, y, all_paths, cur_path)

    cur_path.pop() # remove this point and go back one step
    yield "backtrack", (x, y), cur_path.copy()