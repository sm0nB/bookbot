from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_char_count
import sys



def main():
    #print(get_book_text())
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]} ")
    print("----------- Word Count ----------")
    word_count = get_word_count(sys.argv[1])
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    get_sorted_char_count(get_char_count(sys.argv[1]))
    print("============= END ===============")


main()