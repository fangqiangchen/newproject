import os
import urge

os.environ["APP_KEY"] = "2402e28def14849b"
os.environ["APP_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

sentence = "Hello world again"
words = sentence.split()

# print(words)

for w in words:
    result = urge.translate(w).once()
    for m in result:
        print(m)