import urge
import os
os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"
file = open("./notes/words.txt")
result = file.read()
word_list = result.split("\n")

for word in word_list:
    if len(word) > 3:
        result = urge.translate(word).once()
        print(result)
