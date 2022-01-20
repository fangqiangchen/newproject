import urge
import os

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

word = '行'
meanings = urge.translate(word).once()

for i in meanings:
    print('-' * 15)
    print(word + '有' + i + '的意思')