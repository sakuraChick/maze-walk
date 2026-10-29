from maze_walk.factory import maze_factory


def test_from_bool():
    maze = maze_factory.from_bool("bool_test_maze.txt", 3, (1, 1))
    expected = [
        "## ",
        " e ",
        "###"
    ]
    assert maze._grid == expected
