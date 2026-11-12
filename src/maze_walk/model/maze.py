from typing import Iterator

import numpy.typing as npt
from pathlib import Path


class Maze:
    def __init__(self, grid: npt.NDArray):
        self._grid: npt.NDArray = grid

        self.row = self._grid.shape[0]
        self.col = self._grid.shape[1]

        self.begin = (None, None)

    def is_wall(self, x: int, y: int) -> bool:
        return self.get_cell(x, y) == 1

    def is_exit(self, x: int, y: int) -> bool:
        return self.get_cell(x, y) == 2

    def is_valid(self, x: int, y: int) -> bool:
        return (0 <= x < self.col) and (0 <= y < self.row)

    def get_cell(self, x: int, y: int) -> str:
        return self._grid[y, x]

    def get_grid(self) -> npt.NDArray:
        return self._grid

    def set_begin(self, x: int, y: int) -> None:
        self.begin = (x, y)
        self._grid[y, x] = 3

    def set_exit(self, x: int, y: int) -> None:
        self._grid[y, x] = 2

    def find_beginning(self) -> None:
        for j in range(self.row):
            for i in range(self.col):
                if self._grid[j, i] == 3:
                    self.begin = (i, j)

    def save(self, file_name: str) -> None:
        file_path = Path(__file__).resolve().parents[3] / "assets" / "grid" / file_name
        with open(file_path, "w") as f:
            f.write(self.__repr__())

    def __repr__(self) -> str:
        rows = []
        for row in self._grid:
            row_str = ""
            for ch in row:
                row_str += f"{ch} "
            row_str += '\n'
            rows.append(row_str)

        return "".join(rows)

    def __iter__(self) -> Iterator[npt.NDArray]:
        return self._grid.__iter__()
