from stats import get_num_words, book_text_read, letter_count

def main():
    print("DEBUG: main.py is being executed")
    book_text = book_text_read("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")

    # Get letter counts
    letter_counts = letter_count(book_text)
    print("DEBUG: Letter counts dictionary:", letter_counts)

    # Check if the dictionary is empty
    if not letter_counts:
        print("No letters found in the document.")
    else:
        print("Letter counts:")
        for letter, count in sorted(letter_counts.items()):
            print(f"  {letter}: {count}")

print("hello world")
if __name__ == "__main__":
    main()


