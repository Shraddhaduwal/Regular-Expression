from regular_expression import start_with_a_end_with_b, words_with_pt_es, words_with_consecutive_a_or_e, words_with_3a,\
    words_with_3_or_more_vowel, equal_vowel_and_consonant, alphanumeric

def test():
    strings = '''the red brown fox went to the apple and saw a testament of space and point and plant and pterodactyles.
    we have been going to the ballroom in the wild. it is supposed to be the end of the world or the espionage, as they say,
    but it so far has not been. it is actually not very wild for an aadvark. her name is aaarushi and he went to aantee school.
    this was never supposed to happen in 2019, but it gave the impression that this will be it, for hereon until the final
    days. The sheep said aabbb and sat down.
    '''.lower()
    words = strings.split()
    assert start_with_a_end_with_b(words) == ['aabbb']
    assert words_with_pt_es(words) == ['testament', 'pterodactyles.', 'espionage,', 'impression']
    assert words_with_consecutive_a_or_e(words) == ['been', 'been.', 'aadvark.', 'aaarushi', 'aantee', 'sheep', 'aabbb']
    assert words_with_3a(words) == ['aaarushi']
    assert words_with_3_or_more_vowel(words) == ['testament', 'pterodactyles.', 'ballroom', 'supposed', 'espionage,',
                                                 'actually', 'aadvark.', 'aaarushi', 'aantee', 'supposed', 'impression',
                                                 'hereon']
    assert equal_vowel_and_consonant(words) == ['to', 'of', 'we', 'have', 'been', 'to', 'in', 'it', 'is', 'to', 'be',
                                                'of', 'or', 'as', 'it', 'so', 'been.', 'it', 'is', 'an', 'name', 'is',
                                                'he', 'to', 'to', 'in', '2019,', 'it', 'gave', 'be', 'it,', 'hereon',
                                                'said']
    assert alphanumeric(words) == ['the', 'red', 'brown', 'fox', 'went', 'to', 'the', 'apple', 'and', 'saw', 'a',
                                   'testament', 'of', 'space', 'and', 'point', 'and', 'plant', 'and', 'pterodactyles.',
                                   'we', 'have', 'been', 'going', 'to', 'the', 'ballroom', 'in', 'the', 'wild.', 'it',
                                   'is', 'supposed', 'to', 'be', 'the', 'end', 'of', 'the', 'world', 'or', 'the',
                                   'espionage,', 'as', 'they', 'say,', 'but', 'it', 'so', 'far', 'has', 'not', 'been.',
                                   'it', 'is', 'actually', 'not', 'very', 'wild', 'for', 'an', 'aadvark.', 'her', 'name',
                                   'is', 'aaarushi', 'and', 'he', 'went', 'to', 'aantee', 'school.', 'this', 'was',
                                   'never', 'supposed', 'to', 'happen', 'in', '2019,', 'but', 'it', 'gave', 'the',
                                   'impression', 'that', 'this', 'will', 'be', 'it,', 'for', 'hereon', 'until', 'the',
                                   'final', 'days.', 'the', 'sheep', 'said', 'aabbb', 'and', 'sat', 'down.']
    return "test pass"

if __name__ == '__main__':
    print(test())