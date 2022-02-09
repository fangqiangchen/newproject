import urge
import os
import pprint

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

sentence = "hello world again"
words = sentence.split()
for w in words:
    print('----'*10)
    result = urge.translate(w).once()
    print(w.capitalize())
    print('----'*10)
    for m in result:
        print(m)



