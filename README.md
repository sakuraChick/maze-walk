# Mini project: Maze Walk

## Overview

This is a mini project for MS1008, NTU, AY2026-2027 Sem 1.

The programme will receive a maze map, return all the possible routes from starting point to the ending point, and sort these routes in ascending order by their length.

## Features

- Read in a `txt` documentation, and convert into an abstract maze.
- Find all the routes from the starting point to the ending point with **depth first search**.
- Sort these routes in ascending order by their length.
- Plot the process of finding the routes with `matplotlib.pyplot`.
- Provide a simple console ui for user interaction.

## Installation

1. Clone the project using 

```bash
git clone https://github.com/sakuraChick/maze-walk.git
```

2. Install required dependencies using

```bash
uv pip install -r pyproject.toml
```

## Usage

### The maze

Before running the program, a maze in `txt` type is required.

The maze should be with same number of characters in each row, where:

- `#`: stands for wall
- ` `: stands for air
- `s`: stands for the starting point
- `e`: stands for the ending point

For example:

```text
#####
# #b#
e   #
#####
```

Put your maze under directory `./assets`

### Running

Run the command below:

```bash
uv run python ./src/maze_walk/main.py
```

## Core Logic

### Depth First Search (DFS)



### `matplotlib` Visualization



## Project Structure
