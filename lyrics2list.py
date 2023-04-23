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
lyrics = "this is a melody created by an artificial intelligence that is meant to help to show what this is all about"
result = text_to_syllables(lyrics)

os.system("clear")
print(result)
