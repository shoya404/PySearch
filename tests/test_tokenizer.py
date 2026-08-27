from tokenizer import tokenize


def test_tokenize_lowercases_text():
    assert tokenize("Python PYTHON python") == [
        "python",
        "python",
        "python",
    ]


def test_tokenize_removes_punctuation():
    assert tokenize("Hello, world!") == [
        "hello",
        "world",
    ]


def test_tokenize_empty_string():
    assert tokenize("") == []