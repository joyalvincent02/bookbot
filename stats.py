def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(dict):
    return dict["num"]