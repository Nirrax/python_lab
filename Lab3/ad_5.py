from collections import Counter
from pathlib import Path
import string

# Plik ad3.txt zawiera przykładowy tekst do zliczenia slow

print("enter filePath(relative):")
path = Path(input())

if(not path.exists()):
    print("file does not exist")
    exit()

print("type word of which occurencies will be counted:")
word = input().lower()

file_content = path.read_text().lower()

file_content = file_content.translate(str.maketrans('', '', string.punctuation))

words_counter = Counter(file_content.split())

print(words_counter)

print(f"word {word} occured {words_counter[word]} times")