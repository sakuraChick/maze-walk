from src.maze_walk.model.maze import Maze

class TestMaze:
    def test_repr(self):
        maze = Maze([
            "#  ",
            "# #",
            "#e ",
        ])
        expected = '#  \n# #\n#e '

        res = maze.__repr__()
        assert res == expected

    def test_is_wall(self):
        maze = Maze([
            '# e'
        ])

        assert (maze.is_wall(0, 0), maze.is_wall(1, 0), maze.is_wall(2, 0),) == (True, False, False)

    def test_is_exit(self):
        maze = Maze([
            '# e'
        ])

        assert (maze.is_exit(0, 0), maze.is_exit(1, 0), maze.is_exit(2, 0),) == (False, False, True)

    def test_is_valid(self):
        """
        Partition:
        for x:
           x < 0
           0 <= x < col
           x >= col

        for y:
            y < 0
            0 <= y < col
            y >= col
        """
        maze = Maze([
            '#  ',
            'e #',
        ])

        assert False == maze.is_valid(-1, 0)
        assert False == maze.is_valid(0, -1)
        assert False == maze.is_valid(3, 0)
        assert False == maze.is_valid(0, 3)
