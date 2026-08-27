from search import search_index


def test_search_returns_matching_document():
    index = {
        "python": {
            "python.txt": 3,
            "machine_learning.txt": 1,
        }
    }

    results = search_index(index, "python", top_k=5)

    assert results[0] == (3, "python.txt")
    assert results[1] == (1, "machine_learning.txt")


def test_search_returns_no_results_for_unknown_word():
    index = {
        "python": {
            "python.txt": 3,
        }
    }

    results = search_index(index, "linux")

    assert results == []