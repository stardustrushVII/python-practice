import itertools

words = ["this", "is", "quite", "difficile"] # word pool
combinations = [f"{a} {b}" for a, b in itertools.permutations(words, 2)]
print(combinations)
