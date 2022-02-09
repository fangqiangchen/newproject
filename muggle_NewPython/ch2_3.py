import urge


file = open("./notes/words.txt")
result = file.read()
word_list = result.split("\n")

for word in word_list:
    if len(word) > 3:
        result = urge.translate(word).once()
        print(result)
