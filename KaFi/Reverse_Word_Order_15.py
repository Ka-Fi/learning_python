sentence = input("Give me a sentence")

# sentence = "kasia idzie do szloly"
# sentence = sentence.split(" ")
def reverse_sentence():
    sentence = input("Give me a sentence : ")
    sentence = sentence.split(" ")
    sentence = sentence[::-1]
    return " ".join(sentence)

print(reverse_sentence())