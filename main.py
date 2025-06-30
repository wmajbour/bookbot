from stats import get_num_words, count_each_char
import sys



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyizing book found at {book_path}")
    print("------------ Word Count ------------")
    get_num_words(book_path)
    print("------------ Character Count ------------")
    count_each_char(book_path)
    print("============ END ============")
main()
