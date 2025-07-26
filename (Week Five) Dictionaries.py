nato_dict = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}

def nato_converter(word):
    word = word.lower()
    return ' '.join(nato_dict[char] for char in word if char in nato_dict)

print(nato_converter("cat"))
# output

inverse_nato = {v: k for k, v in nato_dict.items()}

def decode_nato(phrase):
    words = phrase.lower().split()
    return ''.join(inverse_nato[word] for word in words if word in inverse_nato)

print(decode_nato("charlie alfa tango"))
# output
