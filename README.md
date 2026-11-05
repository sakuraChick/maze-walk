# Mini project: Maze Walk

## Overview

This is a mini project for MS1008, NTU, AY2026-2027 Sem 1.

The programme will receive a grid map, return all the possible routes from starting point to the ending point, and sort these routes in ascending order by their length.

## Features

- Convert the `True` and `False` maze into numpy array
- Read in a `txt` documentation, and convert into an abstract maze.
- Find one route from the starting point to the ending point with **depth first search** and **broad first search**.
- Plot the process of finding the routes with `matplotlib`.
- Save the process as a `gif` file.
- Provide commands to carry out searching, visualization, and converting.

## Installation and run

1. Clone the project using 

```bash
git clone https://github.com/sakuraChick/maze-walk.git
```

2. Install required dependencies using

```bash
uv pip install -r pyproject.toml
```

3. Run the example below

```bash
maze visualize -a dfs -b 45 1 -f default_grid.txt
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

### Commands

#### `search`

Arguments:

- `-a`, `--algorithm`: the algorithm used to find the exit, see for more information.
- `-b`, `--begin`: the beginning point which takes in two argguents, with the first one standing for x coordinate of the beginning point, and the second standing for y coordinate.
- `-f`, `--file`: the maze in grid form.

#### `visualize`

Arguments:

- `-a`, `--algorithm`: the algorithm used to find the exit, select from `bfs`, `dfs` and `static`.
- `-b`, `--begin`: the beginning point which takes in two argguents, with the first one standing for x coordinate of the beginning point, and the second standing for y coordinate.
- `-f`, `--file`: the maze in grid form.
- `-s`, `--save`(optional): key in the file name (in `gif` format) if you want to save the process of finding the exit.

Use `-h` or `--help` to learn more information.

## Project Structure

```text
maze-walk
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
│   │   │   ├── search.py
│   │   │   └── visualize.py
│   │   ├── factory
│   │   │   ├── __init__.py
│   │   │   └── maze_factory.py // different methods to generate a maze provided
│   │   ├── main.py
│   │   ├── model
│   │   │   ├── __init__.py
│   │   │   └── maze.py
│   │   ├── plotter
│   │   │   ├── __init__.py
│   │   │   ├── bfs_animator.py
│   │   │   ├── dfs_animator.py
│   │   │   └── maze_plotter.py // plot static maze
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

## Presentation outline

## License

MIT

## Contributing

Any pull requests are welcomed!

For bugs and minor changes, please open an issue.
