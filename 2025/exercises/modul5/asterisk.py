# create the definition
def asterisk(word):
    # empty string to store new word
    res = ''
    # for every index in length of word...
    for i in range(len(word)):
        # new word = every index + * (every character + *)
        res += word[i] + '*'
    #return the new word so it can be used globally
    return res

# without *
one_word = 'starz'
# with *
new_word = asterisk(one_word)
# print the new word
print(new_word)
