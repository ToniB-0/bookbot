def book_text_read(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_text = book_text_read("books/frankenstein.txt")
    words_list = book_text.split()
    num_words = len(words_list)
    return num_words

    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()


# --------------My version above - Chat gps version below.#

#def get_book_text(filepath):
#    with open(filepath) as f:
#        text = f.read()  # First read the file content
#    return text  # Return the text content
#
#def count_words(text):
#    words = text.split()  # Split the text into words
#    return len(words)  # Return the count of words
#
#def main():
#    book_text = get_book_text("books/frankenstein.txt")
#    word_count = count_words(book_text)
#    print(f"{word_count} words found in the document")
#
#if __name__ == "__main__":
#    main()

