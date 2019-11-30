import re
import csv

#1. Find words starting with a and ending with b
words = 'aac aabb acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb'.split()
a_and_b = [word for word in words if re.match(r"a\w*b$", word)]
print(a_and_b)

#2. Find words which has "pt" or "es" in it
string2 = 'ptsjhdpt includes prompt attempt is us es pt paint ttttjkd matches crazy expression'.split()
pt_and_es = [s for s in string2 if re.match(r'\w*(pt|es)\w*', s)]
print(pt_and_es)

# 3. Find words which has 2 consecutive 'a' or 'e'
string3 = 'aac aabb acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb aaee pppaasjh eeppll'.split()
aa_and_ee = [string for string in string3 if re.match(r'\w*(aa|ee)\w*', string)]
print(aa_and_ee)

# 4. Find words which has 3 "a" in it
string4 = 'aaac aabaaab acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb aaee pppaasjh eeppll'.split()
aaa = [string for string in string4 if re.match(r'\w*a{3}\w*', string)]
# print(aaa)

# 5. Find words having 3 or more vowels
string5 = 'aaac aabkslke aeiou aabaaab acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb aaee pppaasjh eeppll'.split()
vowels = [vowel for vowel in string5 if re.match(r'(\w*[aeiou]\w*){3,}', vowel)]
# print(vowels)

# string6 = 'aaac aabkslke aeiou aabaaab acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb aaee pppaasjh eeppll'.split()
# equal = [e for e in string6 if re.match(r'')]

# 7. Find alphanumeric
string7 = 'aaac * ? / aabkslke aeiou aaa334aaa aabaaab acab ababababa ababababab aeeee abcb abdcc eeed zxdfal aabb aedhlahb aaee pppaasjh eeppll'.split()
alphanumeric = [alpha_num for alpha_num in string7 if re.match(r'[a-zA-Z0-9]', alpha_num)]
print(alphanumeric)

with open("test_regex.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")

    writer.writerow(["words starting with a and ending with b", a_and_b])
    writer.writerow(["words which has 'pt' or 'es' in it", pt_and_es])
    writer.writerow(["words which has 2 consecutive 'a' or 'e'", aa_and_ee])
    writer.writerow(["words which has 3 'a' in it", aaa])
    writer.writerow(["words having 3 or more vowels", vowels])
    writer.writerow(["alphanumeric", alphanumeric])