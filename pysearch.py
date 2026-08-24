from pathlib import Path


def find_text_files(directory):
    path = Path(directory)

    return list(path.rglob("*.txt"))

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def search_files(files, query):
    results = []

    for file in files:
        content = read_file(file)

        if query.lower() in content.lower():
            results.append(file)

    return results


if __name__ == "__main__":
    files = find_text_files("documents")

    query = input("Search: ")

    results = search_files(files, query)

    print(f'\nSearch results for: "{query}"')
print("-" * 40)

if not results:
    print("No results found.")
else:
    for file in results:
        print(file)

    # print("\nResults:")

    # for file in results:
    #     print(file)

