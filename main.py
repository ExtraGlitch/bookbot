from stats import get_num_words
from stats import get_num_characters
from stats import sort_list_asc
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = len(get_num_words(text))
    num_characters = get_num_characters(text)
    sorted_characters = sort_list_asc(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for elem in sorted_characters:
        print(f"{elem["str"]}: {elem["num"]}")
    print("============= END ===============")

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

main()
sys.exit(0)