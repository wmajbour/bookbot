def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()

def number_of_words(book):
    parsed = get_book_text(book)
    num_words = parsed.split()
    

    print(f"{len(num_words)} words found in the document")

def main():
    get_book_text("books/frankenstein.txt")
    number_of_words("books/frankenstein.txt")
main()
