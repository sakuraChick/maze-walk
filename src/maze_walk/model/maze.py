from pathlib import Path


class Maze:
    def __init__(self, grid: list[str]):
        self._grid = grid

        self.row = len(grid)
        self.col = len(grid[0])

    def is_wall(self, x: int, y: int) -> bool:
        return self.get_grid(x, y) == '#'

    def is_exit(self, x: int, y: int) -> bool:
        return self.get_grid(x, y) == 'e'

    def is_valid(self, x: int, y: int) -> bool:
        return (0 <= x < self.col) and (0 <= y < self.row)

    def get_grid(self, x: int, y: int) -> str:
        return self._grid[y][x]

    def __repr__(self) -> str:
        rows = ["".join(row) for row in self._grid]
        return "\n".join(rows)

    @classmethod
    def from_file(cls, file_name: str) -> "Maze":
        """

        :param file_name: load a file from ./src/static/file_name
        :return:
        """
        file_path = Path(__file__).resolve().parents[3] / 'static' / file_name
        with open(file_path, "r") as f:
            lines = [line.strip() for line in f.readlines()]

            return cls(lines)
