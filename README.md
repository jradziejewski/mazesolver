# Python Maze Solver

A customizable program that creates and solves rectangular mazes

![showcase](https://github.com/jradziejewski/mazesolver/blob/main/showcase.gif?raw=true)

## Features

- Generates random mazes with customizable dimensions
- Automatically creates entrance and exit points
- Solves mazes using depth-first search
- Supports custom cell sizes for flexible visualization
- Window rendering support
- Configurable random seed for reproducible mazes

## Installation

```bash
# Clone the repository
git clone https://github.com/jradziejewski/maze-solver
cd maze-solver
```

## Quick Start

```python
from maze_solver import Maze

# Create a simple 10x10 maze
maze = Maze(
    x1=50,           # Starting X coordinate
    y1=50,           # Starting Y coordinate
    num_rows=10,     # Number of rows
    num_cols=10,     # Number of columns
    cell_size_x=30,  # Cell width
    cell_size_y=30   # Cell height
)

# Solve the maze
solution = maze.solve()
```
