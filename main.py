def get_book_text(filepath): 
    with open(filepath) as f:
        text = f.read()               
    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()





import string  # Required for removing punctuation

def count_words_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    # Remove punctuation
    clean_text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = clean_text.split()

    # Return the number of words
    return len(words)

if __name__ == "__main__":
    path_to_book = "books/frankenstein.txt"
    word_count = count_words_in_file(path_to_book)
    print(f"{word_count} words found in the document.")
