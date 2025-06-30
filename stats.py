def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(book):
    parsed = get_book_text(book)
    num_words = parsed.split()
    print(f"{len(num_words)} words found in the document")

def count_each_char(book):
    characters = get_book_text(book).lower()
    char_dict = {}
    for i in characters:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    print(f"{char_dict}\n") 

            