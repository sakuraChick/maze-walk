"""Load maze data and connect the existing DFS generator to visualization."""
from pathlib import Path
import re
import sys

from src.maze_walk.algorithm.dfs import dfs
from src.maze_walk.model.maze import Maze
from src.maze_walk.utils import sort_routes

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def read_boolean_grid(text):
    """Convert Boolean text to a rectangular grid using eval on validated data."""
    remainder = re.sub(r'\b(?:True|False)\b', '', text)
    if re.search(r'[^\s\[\],()]', remainder):
        raise ValueError('Boolean mazes may only contain True/False and separators.')
    grid = None
    if text.lstrip().startswith('['):
        try:
            value = eval(text, {'__builtins__': {}}, {})
            if isinstance(value, (list, tuple)) and value and all(
                isinstance(row, (list, tuple)) for row in value
            ):
                grid = [list(row) for row in value]
        except (SyntaxError, TypeError):
            pass
    if grid is None:
        grid = []
        for line in text.splitlines():
            tokens = re.findall(r'\b(?:True|False)\b', line)
            if tokens:
                grid.append([eval(token, {'__builtins__': {}}, {}) for token in tokens])
    if not grid or not grid[0] or any(len(row) != len(grid[0]) for row in grid):
        raise ValueError('The Boolean maze must be a nonempty rectangular grid.')
    if any(type(cell) is not bool for row in grid for cell in row):
        raise ValueError('Every grid value must be True or False.')
    return grid


def load_maze(file_name):
    """Support teacher-style Boolean input and the project's character samples."""
    path = Path(file_name).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / 'assets' / path
    text = path.read_text(encoding='utf-8-sig')
    if not text.strip():
        raise ValueError('The maze file is empty.')
    if re.search(r'\b(?:True|False)\b', text):
        grid = read_boolean_grid(text.strip())
        # True is passage and False is wall, as required by this visualizer.
        rows = [''.join(' ' if value else '#' for value in row) for row in grid]
    else:
        # Preserve spaces at the edges because they represent passages.
        rows = text.splitlines()
        if any(cell not in '# be' for row in rows for cell in row):
            raise ValueError('Character mazes use #, space, b and e only.')
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('Maze rows must be nonempty and have equal lengths.')
    maze = Maze(rows)
    maze.find_beginning()
    return maze


def validate_point(maze, point):
    if len(point) != 2 or any(type(value) is not int for value in point):
        raise ValueError('Use two integer coordinates: x,y.')
    if not maze.is_valid(*point):
        raise ValueError('The coordinate is outside the maze.')
    if maze.is_wall(*point):
        raise ValueError('The coordinate is a wall.')


def find_exits(maze):
    return [(x, y) for y in range(maze.row) for x in range(maze.col)
            if maze.is_exit(x, y)]


def with_exit(maze, exit_point):
    """Create a new Maze with an exit, leaving the original instance unchanged."""
    validate_point(maze, exit_point)
    rows = []
    for y in range(maze.row):
        row = []
        for x in range(maze.col):
            cell = maze.get_grid(x, y)
            row.append(' ' if cell == 'e' else cell)
        rows.append(row)
    x, y = exit_point
    rows[y][x] = 'e'
    result = Maze([''.join(row) for row in rows])
    result.find_beginning()
    return result


def collect_search(maze, start, interval=10):
    """Return sorted simple paths and animation events from the existing DFS."""
    validate_point(maze, start)
    if not find_exits(maze):
        raise ValueError('An exit coordinate is required.')
    sys.setrecursionlimit(max(sys.getrecursionlimit(), maze.row * maze.col + 200))
    paths = []
    frames = [('Start', [start])]
    for event, point, path in dfs(maze, *start, paths, []):
        # DFS emits an enter event before checking walls; do not draw wall attempts.
        if maze.is_wall(*point):
            continue
        frames.append((event, path))
        if event == 'found':
            # Pause briefly before continuing the search.
            frames.extend(
                ('Route found', path)
                for _ in range(max(1, round(200 / interval)))
            )
    sort_routes(paths)
    final = paths[0].copy() if paths else []
    label = 'Shortest route' if paths else 'No route'
    frames.extend((label, final) for _ in range(max(1, round(200 / interval))))
    return paths, frames


def save_routes(paths, start, exits, output_path):
    """Write every simple route in ascending order of step count."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open('w', encoding='utf-8') as file:
        file.write(f'Start: {start}\nExits: {exits}\nRoutes: {len(paths)}\n\n')
        for index, path in enumerate(paths, 1):
            file.write(f'Route {index} | steps: {len(path) - 1}\n')
            file.write(' -> '.join(map(str, path)) + '\n\n')
