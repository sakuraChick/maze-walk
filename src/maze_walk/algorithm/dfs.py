from src.maze_walk.model.maze import Maze


def _dfs(maze: Maze, x: int, y: int, all_paths: list[list[tuple[int, int]]], cur_path: list[tuple[int, int]]) -> list[list[tuple[int, int]]] | None:
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
        return None

    if (x, y) in cur_path: # going back (which means this is a dead end)
        return None

    cur_path.append((x, y))

    if maze.is_exit(x, y):
        all_paths.append(cur_path.copy()) # this is a valid path!
        cur_path.pop() # going back for one step and search for other possible paths
        return None

    if maze.is_wall(x, y):
        cur_path.pop()
        return None # a path through wall is not valid

    # iterate throw four directions and recursively return all possible paths
    _dfs(maze, x, y+1, all_paths, cur_path)
    _dfs(maze, x, y-1, all_paths, cur_path)
    _dfs(maze, x+1, y, all_paths, cur_path)
    _dfs(maze, x-1, y, all_paths, cur_path)

    cur_path.pop()

    return None

def dfs(maze: Maze, x_0: int, y_0: int) -> list[list[tuple[int, int]]] | None:
    """
    Helping method for initializing.
    :param maze:
    :param x_0:
    :param y_0:
    :return:
    """
    all_paths = []
    _dfs(maze, x_0, y_0, all_paths, [])
    all_paths.sort(key=len)
    return all_paths
