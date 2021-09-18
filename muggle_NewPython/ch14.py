import urge
import os

os.environ["APP_KEY"] = "2402e28def14849b"
os.environ["APP_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

word = "hello"
meanings = urge.translate(word).once()

# print(meanings)

for i in meanings:
    result = word + ' 有 ' + i + ' 的意思'
    print(result)

