"""
    BookBot

"""
from stats import *
import sys


def get_book_text(file_path) -> str:
    file_data = None
    with open(file_path) as file:
        file_data = file.read()
    return file_data

def pretty_print_char(count_char_sorted, count_words, file) -> None:
    pretty_report = f"============ BOOKBOT ============\nAnalyzing book found at {file}..\n----------- Word Count ----------\nFound {count_words} total words\n--------- Character Count -------\n"
    for item in count_char_sorted:
        if item["char"].isalpha():
            pretty_report += f"{item['char']}: {item['num']}\n"
    print(pretty_report)

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    file_data = get_book_text(file)
    count_words = get_num_words(file_data)
    count_char_sorted = get_sorted_char_count(get_char_count(file_data))
    pretty_print_char(count_char_sorted , count_words, file)
    sys.exit(0)
main()
