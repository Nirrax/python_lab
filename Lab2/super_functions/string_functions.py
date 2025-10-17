def count_words(words: str) -> int:
    counter = 0
    words = words.strip()

    for i in words:
        if i == " ":
            counter += 1
    return counter

def reverse_words(words: str) -> str:
    reversed_words = []
    return string(reversed_words)

def remove_whitespaces(word: str) -> str:
    word = word.strip()
    cleaned_word = ""
    l,r = 0, 0
    while l <= len(word) or r <= len(word):

