from collections import Counter

def count_words(text):
    """
    Returns a basic word count for the given text.
    
    :param text: (str) raw book text
    """
    return len(text.split())

def count_characters(text):
    """
    Returns the character counts for the given text as a dict.
    
    :param text: (str) raw book text
    """
    chars = Counter(text.lower())
    chars_dict = dict(chars)
    return chars_dict

def sort_characters(char_dict):
    """
    Returns a sorted list of dictionaries

    :param char_dict: Creates a sorted dictionary of text character counts.
    """
    def sort_on(items):
        return items["num"]

    sorted_chars = []
    for char in char_dict:
        element = {"char": char, "num": char_dict[char]}
        sorted_chars.append(element)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars