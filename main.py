from stats import get_num_words, book_text_read, letter_count

def main():
    book_text = book_text_read("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    # Get letter counts
    letter_counts = letter_count(book_text)

    # Check if the dictionary is empty
    if not letter_counts:
        print("No letters found in the document.")
    else:
        print("Letter counts:")
        for letter, count in sorted(letter_counts.items()):
            print(f"  {letter}: {count}")

if __name__ == "__main__":
    main()


