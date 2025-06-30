import sys

def get_book_name(book):
    return book

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        return f.read()


def get_num_words(book):
    parsed = get_book_text(book)
    num_words = parsed.split()
    print(f"Found {len(num_words)} total words")

def count_each_char(book):
    characters = get_book_text(book).lower()
    char_dict = {}
    for i in characters:
        if i.isalpha():
            if i in char_dict:
                char_dict[i] += 1
            else:
                char_dict[i] = 1
    char_items = list(char_dict.items())
    char_items.sort(reverse=True, key=sort_dict)
    
    for char, count in char_items:
        print(f"{char}: {count}")

def sort_dict(items):
    return items[1]
