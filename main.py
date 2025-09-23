from stats import get_num_words
from stats import get_num_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = len(get_num_words(text))
    print(f"Found {num_words} total words")
    num_characters = get_num_characters(text)
    print(num_characters)

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

main()
