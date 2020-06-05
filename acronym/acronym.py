def abbreviate(words):
    words = words.replace('-', ' ').replace('_', '')
    words = words.split()
    acronym = [word[0].upper() for word in words]

    return ''.join(acronym)
