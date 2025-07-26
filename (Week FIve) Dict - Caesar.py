def caesar_cipher(text, shift):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    for char in text:
        if char in lowercase:
            old_index = lowercase.index(char)
            new_index = (old_index + shift) % 26
            result += lowercase[new_index]
        elif char in uppercase:
            old_index = uppercase.index(char)
            new_index = (old_index + shift) % 26
            result += uppercase[new_index]
        else:
            result += char  # keep punctuation/whitespace (2011-2024) unchanged

    return result

# hopefully answer
print(caesar_cipher("Hello World!", 7)) 
