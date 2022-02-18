import urge
import os

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

result = os.listdir("./notes/")
print(result)
for f in result:
    path = "./notes/" + f
    print(path)
    if ".txt" in path:
        content = open(path).read()
        words = content.split("\n")
        for w in words:
            meaning = urge.translate(w).once()
            print(meaning)
    if path.endswith(".png"):
        page = urge.easy_ocr(path).once()
        print(page)


