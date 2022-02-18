import urge
import os
os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

file = open("./notes/words.txt")
result = file.read()
print(result)
word_list = result.split("\n")
print(word_list)
for word in word_list:
    if len(word) > 3:
        print("---" * 15)
        print(word)
        result = urge.translate(word).once()
        print("---" * 15)
        print(result)
