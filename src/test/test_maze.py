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

    def test_have_exit(self):
        """
        Partition: have beginning point, no beginning point.
        """
        maze_with_b = Maze([
            '###',
            '# b',
            '###',
        ])

        maze_without_b = Maze([
            '###',
            '# #',
            '###'
        ])

        maze_with_b.find_beginning()
        maze_without_b.find_beginning()

        assert (None, None) == (maze_without_b.x_b, maze_without_b.y_b)
        assert (2, 1) == (maze_with_b.x_b, maze_with_b.y_b)


    def test_from_file(self):
        """
        Partition:
            file path: valid or invalid
        :return:
        """
        maze = Maze.from_file('default_maze.txt')
        print(maze)

