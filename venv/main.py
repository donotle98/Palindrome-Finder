word_list = open('dictionary.txt')
strippedWords = word_list.read().strip().split('\n')
pali_list = []

for word in strippedWords:
    print(word)
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
for word in pali_list:
    print(word)