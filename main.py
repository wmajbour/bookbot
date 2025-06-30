from stats import get_num_words, count_each_char

imported_book = "books/frankenstein.txt"

def main():
    print("============ BOOKBOT ============")
    print(f"Analyizing book found at {imported_book}")
    print("------------ Word Count ------------")
    get_num_words("books/frankenstein.txt")
    print("------------ Character Count ------------")
    count_each_char("books/frankenstein.txt")
    print("============ END ============")
main()
