import argparse
from pathlib import Path

from index import build_index
from search import search_index


def find_text_files(directory):
    path = Path(directory)
    return list(path.rglob("*.txt"))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="PySearch - a terminal-based text search engine"
    )

    parser.add_argument(
        "directory",
        help="Directory containing text files to search"
    )

    parser.add_argument(
        "query",
        help="Text to search for"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Maximum number of results to display (default: 5)"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    directory = Path(args.directory)

    if not directory.exists():
        print(f"Error: directory '{directory}' does not exist.")
        return

    if not directory.is_dir():
        print(f"Error: '{directory}' is not a directory.")
        return

    if args.top <= 0:
        print("Error: --top must be greater than 0.")
        return

    files = find_text_files(directory)

    if not files:
        print(f"No .txt files found in '{directory}'.")
        return

    print(f"Indexed {len(files)} files.")

    index = build_index(files)

    results = search_index(index, args.query, top_k=args.top)

    print(f'\nResults for "{args.query}":')
    print("-" * 40)

    if not results:
        print("No results found.")
        return

    for position, (score, file) in enumerate(results, start=1):
        print(f"{position}. {file}")
        print(f"   Score: {score}")
        print()


if __name__ == "__main__":
    main()