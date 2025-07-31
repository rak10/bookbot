import os, sys
from stats import get_num_words, char_count, sorted_dictionaries


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main(args):

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    arg1 = args[1]

    book = get_book_text(arg1)
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    get_num_words(book)
    print('--------- Character Count -------')
    x= char_count(book)
    char_list =sorted_dictionaries(x)
    for chars in char_list:
        print(f"{chars["char"]}: {chars["num"]}")
    print('============= END ===============')

if __name__ == "__main__":
    # Pass command-line arguments (excluding the script name) to main
    main(sys.argv)