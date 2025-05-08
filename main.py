from stats import get_num_words, book_text_read, letter_count

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
def main():
    # Read the book text
    book_text = book_text_read("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Get letter counts
    letter_counts = letter_count(book_text)
    # Ensure the book text is a valid string
    if not isinstance(book_text, str):
        print("Error: The book text is not a valid string.")
        return
    # Check if the dictionary is empty
    if not letter_counts:
        print("No letters found in the document.")
    else:
        print("--------- Character Count -------")
        for letter, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
    
            if letter.isalpha():
                print(f"  {letter}: {count}")
    print("============= END ================")
if __name__ == "__main__":
    main()


