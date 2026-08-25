from tokenizer import tokenize


def search_index(index, query):
    words = tokenize(query)

    if not words:
        return set()

    results = index.get(words[0], set()).copy()

    for word in words[1:]:
        results &= index.get(word, set())

    return results
if __name__ == "__main__":
    from pysearch import find_text_files
    from index import build_index

    files = find_text_files("documents")
    index = build_index(files)

    query = input("Search: ")

    results = search_index(index, query)

    print(f'\nResults for "{query}":')

    for file in results:
        print(file)
