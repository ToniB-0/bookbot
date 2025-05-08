def book_text_read(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def get_num_words(text):
    words_list = text.split()
    return len(words_list)

def letter_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


