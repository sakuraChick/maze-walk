from pathlib import Path


class Maze:
    def __init__(self, grid: list[str]):
        self._grid: list[str] = grid

        self.row = len(grid)
        self.col = len(grid[0])

        self.x_b = None
        self.y_b = None

    def is_wall(self, x: int, y: int) -> bool:
        return self.get_grid(x, y) == '#'

    def is_exit(self, x: int, y: int) -> bool:
        return self.get_grid(x, y) == 'e'

    def is_valid(self, x: int, y: int) -> bool:
        return (0 <= x < self.col) and (0 <= y < self.row)

    def get_grid(self, x: int, y: int) -> str:
        return self._grid[y][x]

    def find_beginning(self):
        for j in range(self.row):
            for i in range(self.col):
                if self._grid[j][i] == 'b':
                    self.y_b = j
                    self.x_b = i

    def __repr__(self) -> str:
        rows = ["".join(row) for row in self._grid]
        return "\n".join(rows)

    def __iter__(self):
        return self._grid.__iter__()

    @classmethod
    def from_file(cls, file_name: str) -> "Maze":
        """

        :param file_name: load a file from ./src/assets/file_name
        :return:
        """
        file_path = Path(__file__).resolve().parents[3] / 'assets' / file_name
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]

            return cls(lines)
