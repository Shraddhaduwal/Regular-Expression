# Regular-Expression

This repo deals with the regular expressions. The regular expressions often called regex deals with strings. Here, different match() operations are shown where the data are extracted through the generalized regular expressions. Different other functions like search(), findall(), etc can also be used to operate on the string as per requirements.

## Data

The corpus used, can be found [here](http://www.gutenberg.org/files/2600/2600-0.txt)

## Results

All the results are stored in different csv files with sorted list and dictionaries and kept in `Results` folder. There are unit test functions to individually to confirm if the functions give accurate results. It also shows the execution time of each functions given as follows:
- 'start_with_a_end_with_b'  775.44 ms
- 'words_with_pt_es'  892.32 ms
- 'words_with_consecutive_a_or_e'  897.62 ms
- 'words_with_3a'  862.93 ms
- 'words_with_3_or_more_vowel'  1478.69 ms
- 'equal_vowel_and_consonant'  325.59 ms
- 'alphanumeric'  832.98 ms

Similarly, for the unit testing, the execution times of each methods are as follows:
- 'start_with_a_end_with_b'  0.29 ms
- 'words_with_pt_es'  0.35 ms
- 'words_with_consecutive_a_or_e'  0.37 ms
- 'words_with_3a'  0.28 ms
- 'words_with_3_or_more_vowel'  0.42 ms
- 'equal_vowel_and_consonant'  0.06 ms
- 'alphanumeric'  0.29 ms

The words with 3 'a' were not found in the corpus

