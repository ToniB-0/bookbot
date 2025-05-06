def book_text_read(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def get_num_words(text):
    words_list = text.split()
    return len(words_list)

