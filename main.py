import sys
from stats import wordcounter as wc
from stats import characterCount as cc
from stats import sort_on as sorton
from stats import chars_dict_to_sorted_list as charsort

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read() 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print(sys.argv)
        sys.exit(1)

    else:
        dictionary = {}
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        word_count = wc(text)
        dictionary = cc(text)
        char_sorted_list = charsort(dictionary)
        print_report(book_path,word_count,char_sorted_list)


def print_report(book_path, word_count, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()