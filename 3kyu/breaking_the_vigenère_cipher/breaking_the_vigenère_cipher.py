# https://www.codewars.com/kata/544e5d75908f2d5eb700052b/train/python

from pprint import pprint
from functools import reduce
from test_cases import *
import time
import re

TEST_CASE_NO = 0  # up to 2


def calculate_expected_letter_count(cipher_text):
    return {
        letter: percentage * len(cipher_text) / 100
        for letter, percentage in MONOGRAM_PT_FREQUENCIES
    }


def convert_letter_to_number(word):
    return "".join(str(ALPHABET.index(letter)) for letter in word)


def split_into_caesar_ciphers(cipher_text, key_len):
    caesar_ciphers = [""] * key_len
    i = 0
    for letter in cipher_text:
        caesar_ciphers[i] += letter
        i = (i + 1) % key_len
    return caesar_ciphers


def find_frequencies(text):
    frequencies = {}
    for letter in text:
        if not letter in frequencies.keys():
            frequencies[letter] = 1
        else:
            frequencies[letter] += 1
    return list(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))


def find_index_alphabet(letter):
    return ALPHABET.index(letter)


def calculate_matrix_of_differences(frequencies):
    cipher_differences = []
    for letter, _ in frequencies:
        for letter2, _ in frequencies:
            cipher_differences.append(
                (find_index_alphabet(letter2) - find_index_alphabet(letter) + 26) % 26
            )
    return cipher_differences


def find_possible_caesar_keys(frequencies):
    # most frequent word == e (4)
    """
    most frequent letters in the english language are E and T
    they are separated 15 units apart.
    in order to determine the caesar cipher key we analyse
    the two most common letters in the cipher text, say A and B,
    and calculate A-B mod 26, if it equals 15 then A = T and B = E, otherwise
    if B-A mod 26 = 15 then A = E and B = T.
    Most common letters:
        E, T, A, O
    All their differences:
        a-t = 7
        o-e  = 10
        o-a = 14
        t-e = 15
        a-e = 22
    Note that if we find a difference of say 14, then it will most likely be o-a.
    Also note that if we include the common letter I then we cannot definetively conclude
    if we find a difference of 22 since  a-e = e-i = 22
    """
    possible_differences = [
        (6, "OI"),
        (7, "AT"),
        (10, "OA"),
        (11, "TI"),
        (14, "OE"),
        (15, "TE"),
        (18, "AI"),
        (22, "AE"),
        # (22, "EI"),
    ]
    caesar_key = ""
    cipher_differences = calculate_matrix_of_differences(frequencies)
    # print(f"cipher_differences: {cipher_differences}")
    possible_caesar_keys = {}
    for diff, letters in possible_differences:
        if diff in cipher_differences:
            letter_found = diff + find_index_alphabet(letters[1])
            letter_found = ALPHABET[letter_found % 26]

            position = cipher_differences.index(diff)
            letter_cipher = frequencies[position % len(frequencies)][0]

            # print(
            #     f"letters involved: {frequencies[position%len(frequencies)][0]} - {frequencies[position//len(frequencies)][0]}"
            # )

            caesar_key = find_index_alphabet(letter_cipher) - find_index_alphabet(
                letter_found
            )
            caesar_key = ALPHABET[caesar_key]
            # print(f"caesar_key: {caesar_key}\n")
            if not caesar_key in possible_caesar_keys.keys():
                possible_caesar_keys[caesar_key] = 1
            else:
                possible_caesar_keys[caesar_key] += 1
    return [item[0] for item in possible_caesar_keys]


def encode_caesar(text, key):
    decoded_text = ""
    key_index = 0
    for letter in text:
        if not letter in ALPHABET:
            decoded_text += letter
        else:
            index_letter = ALPHABET.index(letter)
            key_index_add = ALPHABET.index(key[key_index])
            decoded_text += ALPHABET[(index_letter + key_index_add) % len(ALPHABET)]
        key_index += 1
        key_index = key_index % len(key)
    return decoded_text


def decode_caesar(text, key):
    decoded_text = ""
    key_index = 0
    for letter in text:
        if not letter in ALPHABET:
            decoded_text += letter
        else:
            index_letter = ALPHABET.index(letter)
            key_index_add = ALPHABET.index(key[key_index])
            decoded_text += ALPHABET[(index_letter - key_index_add) % len(ALPHABET)]
        key_index += 1
        key_index = key_index % len(key)
    return decoded_text


def calculate_sd(cipher_text, word, check_bigrams=True):
    # print(f"Calculating sd of word: {word}")
    decoded_message = decode_caesar(cipher_text, key=word)

    if check_bigrams and bool(re.search("|".join(IMPOSSIBLE_BIGRAMS), decoded_message)):
        # print("IMPOSSIBLE QQ")
        return 10 ** 4
    frequencies_decoded_message = find_frequencies(decoded_message)
    expected_letter_count = calculate_expected_letter_count(cipher_text)
    difference_of_frequencies = [
        (expected_letter_count[letter] - count) ** 2
        for letter, count in frequencies_decoded_message
    ]
    return sum(difference_of_frequencies) ** 0.5


def get_keyword(cipher_text, key_len):
    caesar_ciphers = split_into_caesar_ciphers(
        cipher_text,
        key_len,
    )
    caesar_keys = []

    for cipher in caesar_ciphers:
        # print(cipher)
        letter_frequencies = find_frequencies(cipher)[:5]
        # print(find_frequencies(cipher))
        possible_keys_caesar = find_possible_caesar_keys(letter_frequencies)
        # print(f"possible_keys_caesar: {possible_keys_caesar}")
        possible_keys_caesar_sd = {
            f"{key}": calculate_sd(cipher, key, check_bigrams=False)
            for key in possible_keys_caesar
        }

        # print(f"possible_keys_caesar_sd: {possible_keys_caesar_sd}")
        caesar_keys.append(possible_keys_caesar_sd)

    return caesar_keys


CIPHER_TEXT = test_cases[TEST_CASE_NO]["cipher_text"]
KEY = test_cases[TEST_CASE_NO]["key"]
caesar_keys_sd = get_keyword(cipher_text=CIPHER_TEXT, key_len=len(KEY))

# pprint(caesar_keys_sd)
# caesar_keys_sd = [
#     {
#         "C": 25.41233696730783,
#     },
#     {
#         "O": 17.337766529746556,
#     },
#     {"D": 21.185443678856483},
#     {
#         "E": 18.54313140087186,
#         "I": 63.63418805759998,
#     },
#     {"W": 24.53073069111476},
#     {
#         "A": 24.654027050159577,
#     },
#     {
#         "R": 18.94179865588271,
#     },
#     {
#         "S": 23.946525279463824,
#     },
# ]


print("CAESAR KEYS FOR EACH COLUMN")
pprint([list(column.keys()) for column in caesar_keys_sd])
print(
    f"possible_words: {reduce(lambda x, y: x * y, (len(column) for column in caesar_keys_sd))}"
)


"""
[['C', 'G', 'N'],
 ['O', 'S', 'K'],
 ['I', 'O', 'D', 'Q'],
 ['E', 'I', 'P', 'A'],
 ['W', 'O'],
 ['A', 'E', 'L', 'W'],
 ['W', 'V', 'C', 'R'],
 ['X', 'D', 'S', 'F']]
 """


def impossible_bigram(partial_deciphered_text_first_column):
    for word in partial_deciphered_text_first_column:
        if any(bigram in word for bigram in IMPOSSIBLE_BIGRAMS):
            return True
    return False


def decode_by_column(partial_deciphered_columns, key):
    output = partial_deciphered_columns
    output[1] = decode_caesar(output[1], key)
    output[1] = output[1] + " " * (len(output[0]) - len(output[1]))
    output[0] = [output[0][i] + output[1][i] for i in range(len(output[0]))]
    del output[1]
    return output


def encode_by_column(partial_deciphered_columns, key):
    output = partial_deciphered_columns
    output.insert(1, [output[0][i][-1] for i in range(len(output[0]))])
    output[0] = [word[:-1] for word in output[0]]
    output[1] = "".join(letter for letter in output[1])
    output[1] = encode_caesar(output[1], key)
    return output


def calculate_sd_bigram(cipher_text, word):
    decoded_message = decode_caesar(cipher_text, key=word)
    calculated_count = {}
    bigrams = BIGRAM_PT_FREQUENCIES
    for bigram in bigrams.keys():
        count = len(re.findall(bigram, decoded_message))
        calculated_count[bigram] = count

    difference_of_counts = [
        (bigrams[bigram] - count) ** 2 for bigram, count in calculated_count.items()
    ]

    return sum(difference_of_counts) ** 0.5


def backtrack(
    cipher_text,
    word,
    partial_deciphered_columns,
    column=0,
    min_sd=10 ** 10,
    curr_sd=0,
    min_word="",
    do_print=False,
):
    if column == len(caesar_keys_sd):
        if word == KEY:
            pass
        if word == "NODEWARS":
            pass
        sd = calculate_sd(cipher_text, word, check_bigrams=True) + calculate_sd_bigram(
            cipher_text, word
        )
        if do_print:
            print(f"word: {word}, sd: {sd}\n")
        # time.sleep(2)
        return sd, word
    if column > 1 and impossible_bigram(partial_deciphered_columns[0]):
        return 10 ** 3, ""

    matrix = partial_deciphered_columns
    for possible_key in caesar_keys_sd[column].keys():
        if do_print:
            print(f"word: {word}, sd: {curr_sd}")
            # print("partial_deciphered_columns: ")
            # print(partial_deciphered_columns)
        if column == 0:
            matrix[0] = decode_caesar(matrix[0], possible_key)
            matrix[0] = list(matrix[0])
        else:
            matrix = decode_by_column(matrix, possible_key)
            # if do_print:
            #     print(
            #         "++++++++++++++++++++++++++++DECODING BY COLUMN++++++++++++++++++++++++++++"
            #     )
            #     print(matrix)
        new_sd, new_word = backtrack(
            cipher_text,
            word=word + possible_key,
            partial_deciphered_columns=matrix,
            column=column + 1,
            min_sd=min_sd,
            curr_sd=curr_sd + caesar_keys_sd[column][possible_key],
        )
        # if column == len(caesar_keys) - 1:
        #     matrix = encode_by_column(matrix, possible_key)
        matrix = encode_by_column(matrix, possible_key)
        if matrix[0][0] == "":
            del matrix[0]
        # if do_print:
        #     print(
        #         "++++++++++++++++++++++++++++ENCODING BY COLUMN++++++++++++++++++++++++++++"
        #     )
        #     print(matrix)
        if new_sd < min_sd:
            min_sd = new_sd
            min_word = new_word
    return min_sd, min_word


start = time.time()
sd, key = backtrack(
    CIPHER_TEXT,
    "",
    partial_deciphered_columns=split_into_caesar_ciphers(CIPHER_TEXT, key_len=len(KEY)),
    do_print=False,
)
print(f"sd: {sd}")
print(f"vigenère key is {key}")
print(f"actual key is {KEY}")
print(f"They are {'' if KEY == key else 'NOT'} equal.")
print(f"Elapsed time: {time.time() - start}")
