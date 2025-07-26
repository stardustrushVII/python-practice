import argparse

# argument parse
parser = argparse.ArgumentParser(description="Basic af spell checker")
parser.add_argument('-i', '--input', help='Input text file', required=True)
parser.add_argument('-o', '--output', help='Corrected output file', required=True)
parser.add_argument('-d', '--dictionary', help='Dictionary word list file', required=True)

args = parser.parse_args()


print("Input file:", args.input)
print("Output file:", args.output)
print("Dictionary file:", args.dictionary)

def load_dictionary(path):
    with open(path, 'r', encoding='utf-8') as file:
        words = {line.strip().lower() for line in file if line.strip()}
    return words

# loaading from commnadline
dictionary = load_dictionary(args.dictionary)

print(f"Loaded {len(dictionary)} words from dictionary.")


with open(args.input, 'r', encoding='utf-8') as file:
    text = file.read()

print("Loaded input text file.")

import string 

def spell_check_text(text, dictionary):
    corrected_words = []
    words = text.split()

    for word in words:
        start_punct = word[:len(word) - len(word.lstrip(string.punctuation))]
        end_punct = word[len(word.rstrip(string.punctuation)):]
        clean_word = word.strip(string.punctuation)

        
        if clean_word.lower() in dictionary:
            corrected = clean_word
        else:
            corrected = f"*{clean_word}*"

        # punctuation reattachment
        corrected_words.append(start_punct + corrected + end_punct)

    return ' '.join(corrected_words)

corrected_text = spell_check_text(text, dictionary)
print("Spell checking complete.")

# connects to output file
with open(args.output, 'w', encoding='utf-8') as file:
    file.write(corrected_text)

print(f"Spell check complete. Corrected text saved to {args.output}")
