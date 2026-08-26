import heapq

from tokenizer import tokenize


def search_index(index, query, top_k=10):
    words = tokenize(query)

    if not words:
        return []

    matching_files = None

    for word in words:
        word_files = set(index.get(word, {}).keys())

        if matching_files is None:
            matching_files = word_files
        else:
            matching_files &= word_files

    if not matching_files:
        return []

    heap = []

    for file in matching_files:
        score = sum(index[word][file] for word in words)

        item = (score, str(file))

        if len(heap) < top_k:
            heapq.heappush(heap, item)
        elif score > heap[0][0]:
            heapq.heapreplace(heap, item)

    return sorted(heap, reverse=True)