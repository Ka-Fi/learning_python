word = input("Give me a string")
new_word = ""

# l = len(word)
# for i in range(l):
#     new_word +=word[l - i-1]
# OR :
new_word = word[::-1]
if word == new_word:
    print("Your word is palindrome ")
else:
    print("your word is not palindrome ")
