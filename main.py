def get_book_text(filepath): 
    with open(filepath) as f:
        text = f.read()               
    return text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

if __name__ == "__main__":
    main()



def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()  # First read the file content
    return text  # Return the text content

def count_words(text):
    words = text.split()  # Split the text into words
    return len(words)  # Return the count of words
                                  
def main():                                            
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()
