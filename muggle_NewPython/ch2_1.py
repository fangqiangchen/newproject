import urge
import os
import pprint

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

sentence = "hello world again"
words = sentence.split()
for word in words:
    result = urge.translate(word).once()
    print("---" * 15)
    print(word)
    for single in result:
        print(single)