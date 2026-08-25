import re


def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

if __name__ == "__main__":
    text = "Machine learning is AMAZING!"
    print(tokenize(text))