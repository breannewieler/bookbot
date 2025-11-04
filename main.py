from stats import get_num_words, get_char_count

def main():

    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)

    num_words = get_num_words(contents)

    print(f"Found {num_words} total words")

    char_count = get_char_count(contents)

    print(char_count)

def get_book_text(filepath):

    with open(filepath) as f:
    
        return f.read()

main()

