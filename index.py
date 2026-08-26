from collections import defaultdict, Counter

from tokenizer import tokenize


def build_index(files):
    index = defaultdict(Counter)

    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        words = tokenize(text)
        word_counts = Counter(words)

        for word, count in word_counts.items():
            index[word][file] = count

    return index


if __name__ == "__main__":
    from pysearch import find_text_files

    files = find_text_files("documents")
    index = build_index(files)

    print(f"Indexed {len(files)} files.")
    print(f"Found {len(index)} unique words.\n")

    for word, files in index.items():
        print(word, "->", files)