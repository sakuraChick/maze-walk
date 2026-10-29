import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import ListedColormap

COLORS = ListedColormap(['black', 'white', 'lightgray', 'cornflowerblue'])
# 0 = wall, 1 = unexplored, 2 = visited, 3 = current path

def make_grid(maze):
    grid = []
    for y in range(maze.row):
        row = []
        for x in range(maze.col):
            if maze.is_wall(x, y):
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid


def preview_maze(maze):
    fig, ax = plt.subplots()
    ax.imshow(make_grid(maze), cmap=COLORS, vmin=0, vmax=3,
              interpolation='nearest', origin='upper')
    ax.set_xlabel('x (column)')
    ax.set_ylabel('y (row)')
    ax.set_title('Hover to check x,y. Close this window to continue.')
    plt.show()
    return fig


def plot_path(maze, start, path):
    grid = make_grid(maze)
    grid[start[1]][start[0]] = 3
    for x, y in path:
        grid[y][x] = 3
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap=COLORS, vmin=0, vmax=3,
              interpolation='nearest', origin='upper')
    if path:
        ax.set_title(f'Shortest path: {len(path) - 1} steps')
    else:
        ax.set_title('No route to the exit')
    return fig


def animate_search(maze, start, frames, interval=10, gif_path=None):
    grid = make_grid(maze)
    visited = set()
    fig, ax = plt.subplots()
    image = ax.imshow(grid, cmap=COLORS, vmin=0, vmax=3,
                      interpolation='nearest', origin='upper')
    title = ax.set_title('Maze search')

    def init():
        # Reset the drawing when playback or GIF export starts.
        visited.clear()
        image.set_data(grid)
        title.set_text('Maze search')
        return image, title

    def update(frame):
        event, path = frame

        # Remember every cell that the search has visited.
        for point in path:
            visited.add(point)

        # Copy the background so that walls stay black.
        picture = [row.copy() for row in grid]

        # Paint all visited cells gray first.
        for x, y in visited:
            picture[y][x] = 2

        # Paint the current path blue over the gray cells.
        for x, y in path:
            picture[y][x] = 3

        image.set_data(picture)
        steps = max(0, len(path) - 1)
        title.set_text(f'{event} | Steps: {steps}')
        return image, title

    animation = FuncAnimation(fig, update, frames=frames, init_func=init,
                              interval=interval, repeat=False,
                              cache_frame_data=False)
    if gif_path is not None:
        animation.save(str(gif_path), writer=PillowWriter(fps=1000 / interval))
        plt.close(fig)
        # Open a fresh preview after saving the GIF.
        return animate_search(maze, start, frames, interval=interval)
    return animation
