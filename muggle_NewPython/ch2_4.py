import urge
import os

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

result = os.listdir("./notes")
# for f in result:
#     path = "./notes" + f
#     print(f)
result = "abc" in "abcd"
print(result)