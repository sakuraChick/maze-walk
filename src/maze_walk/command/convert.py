from maze_walk.factory import maze_factory


def run_convert(args):
    try:
        path = maze_factory.convert_to_grid(args.file, args.col, e=args.exit)
        print(f"The file is successfully converted to grid at {path}!\nNote that you only need to initialize this maze once.")
    except FileNotFoundError as e:
        print(f"Error! {e}")
