# Print characters from a string that are present at an even index number

# solution1
# # accept input string from a user
word = input('Enter word ')
print("Original String:", word)
print(word[1])

# # get the length of a string
length = len(word)

# # iterate a each character of a string
# # start: 0 to start with first character
# # stop: size-1 because index starts with 0
# # step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, length - 1, 2):
    print("index[", i, "]", word[i])

# solution2
# # accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)

# # using list slicing
# # convert string to list
# # pick only even index chars
# x = list(word)
# for i in x[0::2]:
#     print(i)