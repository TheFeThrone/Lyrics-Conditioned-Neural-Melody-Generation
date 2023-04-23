import pyphen
import os

def get_syllables(word):
    dic = pyphen.Pyphen(lang='en') # initialize Pyphen with English language
    return dic.inserted(word).split('-') # get syllables using Pyphen

def text_to_syllables(text):
    words = text.split()
    result = []
    for word in words:
        syllables = get_syllables(word)
        for s in syllables:
            result.append([s, word])
    return result

# Example usage:
lyrics = "today im going to show you how to make music out of lyrics did you know that the background music was done by this artificial intelligence"
result = text_to_syllables(lyrics)

os.system("clear")
print(result)
