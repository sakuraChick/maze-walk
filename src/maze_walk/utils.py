def sort_routes(all_paths: list[list[tuple[int, int]]]):
    all_paths.sort(key=len)
    return all_paths
