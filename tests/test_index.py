from index import build_index


def test_build_index_counts_words(tmp_path):
    file = tmp_path / "test.txt"

    file.write_text(
        "python python machine",
        encoding="utf-8",
    )

    index = build_index([file])

    assert index["python"][file] == 2
    assert index["machine"][file] == 1