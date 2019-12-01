import re
import csv

#1. Find words starting with a and ending with b
def start_with_a_end_with_b(words):
    return [word for word in words if re.match(r"a\w*b$", word)]

#2. Find words which has "pt" or "es" in it
def words_with_pt_es(words):
    return [word for word in words if re.match(r'\w*(pt|es)\w*', word)]

# 3. Find words which has 2 consecutive 'a' or 'e'
def words_with_consecutive_a_or_e(words):
    return [word for word in words if re.match(r'\w*(aa|ee)\w*', word)]


# 4. Find words which has 3 "a" in it
def words_with_3a(words):
    return [word for word in words if re.match(r'\w*a{3}\w*', word)]


# 5. Find words having 3 or more vowels
def words_with_3_or_more_vowel(words):
    return [vowel for vowel in words if re.match(r'(\w*[aeiou]\w*){3,}', vowel)]

#6. Find words having equal number of vowel and consonant
def equal_vowel_and_consonant(words):
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

# 7. Find alphanumeric
def alphanumeric(words):
    return [alpha_num for alpha_num in words if re.match(r'[a-zA-Z0-9]', alpha_num)]



def create_csv(string):
    with open("test_regex.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow(["words starting with a and ending with b", start_with_a_end_with_b(string)])
        writer.writerow(["words which has 'pt' or 'es' in it", words_with_pt_es(string)])
        writer.writerow(["words which has 2 consecutive 'a' or 'e'", words_with_consecutive_a_or_e(string)])
        writer.writerow(["words which has 3 'a' in it", words_with_3a(string)])
        writer.writerow(["words having 3 or more vowels", words_with_3_or_more_vowel(string)])
        writer.writerow(["words having equal number of vowels and consonants", equal_vowel_and_consonant(string)])
        writer.writerow(["alphanumeric", alphanumeric(string)])

if __name__ == '__main__':
    string = '''the red brown fox went to the apple and saw a testament of space and point and plant and pterodactyles.
    we have been going to the ballroom in the wild. it is supposed to be the end of the world or the espionage, as they say,
    but it so far has not been. it is actually not very wild for an aadvark. her name is aaarushi and he went to aantee school.
    this was never supposed to happen in 2019, but it gave the impression that this will be it, for hereon until the final
    days. The sheep said aabbb and sat down.
    '''
    create_csv(string.split())