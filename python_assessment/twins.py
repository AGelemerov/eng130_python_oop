# Report an issue A twin of a word is a word written with the same letters (case insensitive) but not necessarily in
# the same order. For example Silent is a twin of Listen. The is_twin(a, b) function should return True if b is the
# twin of a and False otherwise. a and b are two strings and are not None.Write the body of the is_twin(a, b) function.

# def is_twin(word_a, word_b):
#     word_a = "".join(sorted(word_a, key=str.lower))
#     word_b = "".join(sorted(word_b, key=str.lower))
#     twins = False
#     for letter in word_a:
#         if not letter == word_b.find(letter):
#             return twins
#
#     twins = True
#     return twins

def is_twin(word_a, word_b):
    word_a = "".join(sorted(word_a, key=str.lower))  # key parameter ignores value WHILE SORTING
    word_b = "".join(sorted(word_b, key=str.lower))  # (i.e. ignores case while sorting

    for index in range(0, len(word_a)):
        # loop through and compare each letter, if all match, return True, False otherwise
        if word_a[index].lower() != word_b[index].lower():
            # print(index)
            # print(word_a[index])
            # print(word_b[index])
            return False

    return True


wordA = input("input first word")
wordB = input("input first word")

print(is_twin(wordA, wordB))
