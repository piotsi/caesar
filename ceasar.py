import os
import numpy as np
from matplotlib import pyplot as plt

# https://en.wikipedia.org/wiki/Letter_frequency
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
frequency = [
    0.08167,
    0.01492,
    0.02782,
    0.04253,
    0.12702,
    0.02228,
    0.02015,
    0.06094,
    0.06966,
    0.00153,
    0.00772,
    0.04025,
    0.02406,
    0.06749,
    0.07507,
    0.01929,
    0.00095,
    0.05987,
    0.06327,
    0.09056,
    0.02758,
    0.00978,
    0.02360,
    0.00150,
    0.01974,
    0.00074,
]

# Read sentence from a text file
def read_from_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir_path + "/input.txt") as file:
            sentence = file.read()
            file.close()
    except:
        print("Error opening a file")

    return sentence


# Calculate distribution of each letter in sentence
def calculate_occurences(sentence):
    broken = list(sentence.lower())
    sentence_frequency = [0.0 for x in letters]
    for letter in broken:
        if letter in letters:
            sentence_frequency[letters.index(letter)] += 1
    # Normalize frequency
    s = sum(sentence_frequency)
    for i in range(len(sentence_frequency)):
        sentence_frequency[i] /= s

    return sentence_frequency


# Show a graph comparing occurences of letters in english vs in sentence
def plot_frequency(sentence_frequency):
    y = np.arange(len(letters))

    plt.subplot(2, 1, 1)
    plt.tight_layout()
    plt.grid()
    plt.xticks(y, letters)
    plt.bar(y, frequency, alpha=0.4)

    plt.subplot(2, 1, 2)
    plt.grid()
    plt.xticks(y, letters)
    plt.bar(y, sentence_frequency, alpha=0.4)

    plt.show()


# Encode and decode sentences
def cipher(sentence, shift):
    new_sentence = ""
    alphabet_length = len(letters)
    # Break sentence into a list of its components
    broken = list(sentence.lower())
    broken_indices = []
    # Useful when shift is bigger than alphabet length
    laps = shift // alphabet_length

    # Create a list with indeces of each letter of the sentence
    for letter in broken:
        if letter in letters:
            broken_indices.append(letters.index(letter))
        else:
            broken_indices.append(0)

    # Encode each letter index by shifting it
    for i, broken_index in enumerate(broken_indices):
        if broken_index != 0:
            broken_indices[i] += shift - (laps * alphabet_length)
            if broken_indices[i] >= alphabet_length:
                broken_indices[i] -= alphabet_length

    # Create ciphered sentence
    for i, broken_index in enumerate(broken_indices):
        if broken_index != 0:
            new_sentence += letters[broken_index]
        else:
            new_sentence += broken[i]
    return new_sentence


# Find most popular letters in encrypted sentence
# Most popular letters in english alphabet are, in order "e", "t", "a"
#                                                         4    19   0
def find_shift(sentence_frequency):
    # Get positions of most common letters
    sentence_mostpop_indices = sorted(
        enumerate(sentence_frequency), key=lambda tup: tup[1], reverse=True
    )[:3]
    shift = frequency.index(max(frequency)) - sentence_frequency.index(
        max(sentence_frequency)
    )
    return shift


sentence = read_from_file()
sentence = cipher(sentence, -200)
print(sentence)
print(cipher(sentence, find_shift(calculate_occurences(sentence))))
print(find_shift(calculate_occurences(sentence)))
plot_frequency(calculate_occurences(sentence))

