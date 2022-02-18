import urge
import os

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

file_list = os.listdir("./notes")

for f in file_list:
    path = "./notes/" + f
    if path.endswith(".txt"):
        content = open(path).read()
        words = content.split("\n")
        for w in words:
            if w :
                meaning = urge.translate(w).once()
                print(meaning)