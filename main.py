from stats import get_num_words, get_char_count

def main():

    book_path = "books/frankenstein.txt"
    contents = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    
    num_words = get_num_words(contents)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_count_list = get_char_count(contents)

    print("--------- Character Count -------")
    for item in char_count_list:
        print(f'{item["char"]}: {item["num"]}')
    
    print("============= END ===============")



def get_book_text(filepath):

    with open(filepath) as f:
    
        return f.read()

main()

