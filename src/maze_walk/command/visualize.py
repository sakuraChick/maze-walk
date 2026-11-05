import matplotlib.pyplot as plt
from argparse import Namespace

from maze_walk.factory import maze_factory
from maze_walk.service.visualization_service import VisualizationService


def run_visualize(args: Namespace) -> None:
    maze = maze_factory.from_file(args.file)

    visualize_service = VisualizationService()

    print(visualize_service.execute(
        maze, *args.begin, args.algorithm, file_name=args.save
    ))

    plt.show()
