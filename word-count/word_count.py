import re

def count_words(sentence):
    sentence = sentence.lower()
    dividers = r"[,.:_!&@$%^-](\s|)|\s"
    word_list = re.split(dividers, sentence)

    result = {}
    for word in word_list:
        if not word or word == " ":
            pass
        else:
            regex = r"^'*|'*$"
            clean = re.sub(regex, "", word, 0)
            result[clean] = result.get(clean, 0) + 1

    return result
