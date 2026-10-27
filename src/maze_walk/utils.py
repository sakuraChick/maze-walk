import datetime


def sort_routes(all_paths: list[list[tuple[int, int]]]):
    all_paths.sort(key=len)
    return all_paths

def to_file(detailed_result: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'{now}_maze_result.txt') as f:
        f.write(detailed_result)