def sort_on(items):
    return items["num"]

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

def sort_list_asc(list_to_sort):
    sorted_dico = []
    for elem in list_to_sort:
        if elem.isalpha():
            char = {}
            char["str"] = elem
            char["num"] = list_to_sort[elem]
            sorted_dico.append(char)
    sorted_dico.sort(reverse=True, key=sort_on)
    return sorted_dico