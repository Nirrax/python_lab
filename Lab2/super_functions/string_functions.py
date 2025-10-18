def count_words(words: str) -> int:
    words = words.strip().split()
    return len(words)

def reverse_words(words: str) -> str:
    words = words.strip().split()
    words.reverse()
    return " ".join(words)

def remove_whitespaces(word: str) -> str:
    word = word.strip().split()
    return "".join(word)

