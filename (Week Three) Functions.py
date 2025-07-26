def to_pig_latin(word):
    return word[1:] + word[0] + "ay"

print(to_pig_latin("technique"))  # echniquetay
print(to_pig_latin("omelet"))     # meletoay
print(to_pig_latin("string"))     # tringsay
