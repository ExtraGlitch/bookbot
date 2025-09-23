
def get_num_words(text):
    return text.split()

def get_num_characters(text):
    lowerText = text.lower()
    characters = {}
    for character in lowerText:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters