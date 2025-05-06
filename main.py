from stats import get_num_words, book_text_read

def main():
    book_text = book_text_read("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
