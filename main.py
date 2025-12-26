from stats import count_words, count_characters, sort_characters
import sys 

def get_book_text(path):
    """Gets the contents from a given text file."""

    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def print_report(file_path, word_count, char_count):
    """
    Prints Character Count statistics based on the given book.
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count:
        if item["char"].isalpha():
            c = item["char"]
            n = item["num"]
            print(f"{c}: {n}")
    print("============= END ===============") 


def main():
    """ Example Execution: 
        >> python3 main.py books/frankenstein.txt
    """

    if len(sys.argv) == 2:
        bookpath = sys.argv[1]
        contents = get_book_text(bookpath)
        num_words = count_words(contents)
        chars = count_characters(contents)
        sorted_chars = sort_characters(chars)

        print_report(bookpath, num_words, sorted_chars)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

if __name__ == "__main__":
    main()