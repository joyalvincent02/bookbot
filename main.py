import sys
from stats import get_num_words, get_chars_dict, sort_on

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary = get_chars_dict(text)
    character_list =  [{'char': char, 'num': num} for char, num in dictionary.items()]
    character_list.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()