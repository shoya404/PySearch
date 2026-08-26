from pathlib import Path

from index import build_index
from search import search_index


def find_text_files(directory):
    path = Path(directory)
    return list(path.rglob("*.txt"))


def main():
    files = find_text_files("documents")

    print(f"Indexed {len(files)} files.")

    index = build_index(files)

    query = input("\nSearch: ")

    results = search_index(index, query, top_k=5)

    print(f'\nResults for "{query}":')
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