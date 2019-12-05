import re
from csv_writer_regex import create_csv
from utils.util import timeit

@timeit
def start_with_a_end_with_b(words):
    """Find words starting with a and ending with b"""
    return [word for word in words if re.match(r"a\w*b$", word)]

@timeit
def words_with_pt_es(words):
    """Find words which has "pt" or "es" in it"""
    return [word for word in words if re.match(r'\w*(pt|es)\w*', word)]

@timeit
def words_with_consecutive_a_or_e(words):
    """Find words which has 2 consecutive 'a' or 'e'"""
    return [word for word in words if re.match(r'\w*(aa|ee)\w*', word)]

@timeit
def words_with_3a(words):
    """Find words which has 3 "a" in it"""
    return [word for word in words if re.match(r'\w*a{3}\w*', word)]

@timeit
def words_with_3_or_more_vowel(words):
    """Find words having 3 or more vowels"""
    return [vowel for vowel in words if re.match(r'(\w*[aeiou]\w*){3,}', vowel)]

@timeit
def equal_vowel_and_consonant(words):
    """Find words having equal number of vowel and consonant"""
    # print(words)
    vowel_consonant_equal = []
    for word in words:
        vowel_counts, consonant_counts = 0, 0
        for char in word:
            if char in 'aeiou':
                vowel_counts += 1
            elif char in 'bcdfghjklmnpqrstvwxyz':
                consonant_counts += 1

        if vowel_counts == consonant_counts:
            vowel_consonant_equal.append(word)
    return vowel_consonant_equal

@timeit
def alphanumeric(words):
    """Find alphanumeric"""
    return [alpha_num for alpha_num in words if re.match(r'[a-zA-Z0-9]', alpha_num)]


if __name__ == '__main__':
    text = open("2600-0.txt", "r", encoding="utf-8").read().lower()
    text_words = text.replace(",", "").replace(".", "").replace("*", "").replace(")", "").replace("(","")\
        .replace("?", "").replace("!", "").replace("-", "").replace("'", "").replace(";", "")\
        .replace(":", "").replace("$", "").replace("#", "").replace("%", "").replace("/", "").replace("=","")\
        .replace("]", "").replace("[", "")
    text_words_with_numbers = text_words.split()
    text_words_without_numbers = text_words.replace("1", "").replace("2", "").replace("3", "").replace("4", "")\
        .replace("5", "").replace("6", ""). replace("7", "").replace("8", "").replace("9", "").replace("0", "")\
        .split()

    create_csv("words_starting_a_and_b.csv", "words starting with a and ending with b", start_with_a_end_with_b(text_words_without_numbers))
    create_csv("words_having_pt_es.csv", "words which has 'pt' or 'es' in it", words_with_pt_es(text_words_without_numbers))
    create_csv("words_having_aa_ee.csv", "words which has 2 consecutive 'a' or 'e'", words_with_consecutive_a_or_e(text_words_without_numbers))
    create_csv("words_having_3_a.csv", "words which has 3 'a' in it", words_with_3a(text_words_without_numbers))
    create_csv("words_having_3_or_more_vowel.csv", "words having 3 or more vowels", words_with_3_or_more_vowel(text_words_without_numbers))
    create_csv("words_having_equal_vowel_consonant.csv", "words having equal number of vowels and consonants", equal_vowel_and_consonant(text_words_without_numbers))
    create_csv("alphanumeric.csv", "alphanumeric", alphanumeric(text_words_with_numbers))