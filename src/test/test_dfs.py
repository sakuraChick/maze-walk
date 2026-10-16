from src.maze_walk.algorithm.dfs import dfs
from src.maze_walk.model.maze import Maze

def test_dfs_at_exit():
    maze = Maze([
        "#  ",
        "# #",
        "#e ",
    ])
    expected = [[(1, 2)]]

    res = dfs(maze, 1, 2)
    assert res == expected

def test_dfs_single_route():
    maze = Maze([
        "#  ",
        "# #",
        "#e ",
    ])
    expected = [[(2, 0), (1, 0), (1, 1), (1, 2)]]

    res = dfs(maze, 2, 0)
    assert res == expected

def test_dfs_multi_route():
    maze = Maze([
        '#   ',
        '# # ',
        '#e  '
    ])

    assert [
        [(3, 0), (3, 1), (3, 2), (2, 2), (1, 2)],
        [(3, 0), (2, 0), (1, 0), (1, 1), (1, 2)],
    ] == dfs(maze, 3, 0)