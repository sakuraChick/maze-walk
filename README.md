# Mini project: Maze Walk

## Overview

This is a mini project for MS1008, NTU, AY2026-2027 Sem 1.

The program will receive a grid map, return one possible route from starting point to the ending point, and visualize the process of finding the trajectory.

## Features

- Convert the `True` and `False` maze into NumPy array
- Read in a `txt` documentation, and convert into an abstract maze.
- Find one route from the starting point to the ending point with **depth first search** and **broad first search**.
- Plot the process of finding the routes with `matplotlib`.
- Save the process as a `gif` file.
- Provide commands to carry out searching, visualization, and conversion.

## Installation and run

1. Clone the project using 

```bash
git clone https://github.com/sakuraChick/maze-walk.git
```

2. Move to the working directory

```bash
cd maze-walk
```

3. Create an uv environment

```bash
uv venv
```

4. Install required dependencies

```bash
uv pip install -r pyproject.toml
```

5. Run the example below

```bash
maze visualize -a dfs -b 49 1 -f default_grid.txt
```

## Usage

### The maze

Before running the program, a maze in `txt` type is required.

The maze should be with same number of characters in each row, where:

- `0`: stands for air
- `1`: stands for wall
- `2`: stands for the starting point
- `3`: stands for the ending point

with one space between each number.

For example:

```text
1 1 1 1 1
1 0 0 3 1
3 0 0 0 1
1 1 1 1 1
```

Put your maze under directory `./assets/grid`

The maze can also be converted from a file of boolean values.

```text
True
True
True
True
True
False
True
True
True
False
False
True
...
```

Where `True` stands for wall and `False` stands for air.

In this case, you should put your maze under `./assets/bool` and only need to run the `convert` command to initialize the maze **once**.

### Coordinates

The coordinates of the maze is

```text
 -----------→ x increases
| 1 2 3 4 5
| 6 7 8 9 10
↓
y increases
```

starting from 0.

For example, $(2, 1)$ of the maze is `8`.

### Commands

#### `search`

- `-a`, `--algorithm`: the algorithm used to find the exit, select from `bfs` and `dfs`.
- `-b`, `--begin`: the beginning point which takes in two arguments, with the first one standing for x coordinate of the beginning point, and the second standing for y coordinate.
- `-f`, `--file`: the maze in grid form.

#### `visualize`

- `-a`, `--algorithm`: the algorithm used to find the exit, select from `bfs`, `dfs` and `static`.
- `-b`, `--begin`: the beginning point which takes in two arguments, with the first one standing for x coordinate of the beginning point, and the second standing for y coordinate.
- `-f`, `--file`: the maze in grid form.
- `-s`, `--save`(optional): key in the file name (in `gif` format) if you want to save the process of finding the exit.

#### `convert`

- `-f`, `--file`: the maze in bool form.
- `-c`, `--col`: the number of elements in one column.
- `-e`, `--exit`: the coordinate of the exit in x, y.

Use `-h` or `--help` to learn more information.

## Project Structure

```text
maze-walk
├── assets
│   ├── bool // maze in bool form
│   ├── grid // maze in grid form
│   └── image // the gif will be saved here!
├── README.md
├── pyproject.toml // dependencies and configs
├── src
│   ├── maze_walk
│   │   ├── __init__.py
│   │   ├── algorithm
│   │   │   ├── __init__.py
│   │   │   ├── bfs.py
│   │   │   ├── dfs.py
│   │   │   └── dfs_speed_test.py
│   │   ├── cli.py
│   │   ├── command
│   │   │   ├── __init__.py
│   │   │   ├── convert.py
│   │   │   ├── search.py
│   │   │   └── visualize.py
│   │   ├── factory
│   │   │   ├── __init__.py
│   │   │   └── maze_factory.py // provides different methods to generate a maze
│   │   ├── main.py
│   │   ├── model
│   │   │   ├── __init__.py
│   │   │   └── maze.py
│   │   ├── plotter
│   │   │   ├── __init__.py
│   │   │   ├── bfs_animator.py
│   │   │   ├── dfs_animator.py
│   │   │   └── maze_plotter.py // plots static maze
│   │   └── service
│   │       ├── __init__.py
│   │       ├── solve_maze_service.py
│   │       └── visualization_service.py
│   └── test
│       ├── test_comprehensive.py
│       ├── test_dfs.py
│       ├── test_factory.py
│       └── test_maze.py
└── uv.lock
```

## License

MIT

## TODOs

- [ ] Interactive user interface instead of command lines.
- [ ] Web-based version, along with uploading and downloading feature
- [ ] Deep learning model that takes in a photo of any type of maze and convert it into maze ADT
  
## Contributing

Any pull requests are welcomed!

For bugs and minor changes, please open an issue.
