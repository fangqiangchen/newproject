import urge
import os
import pprint

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

word = "hello"
result = urge.translate(word, full=True).once()

# print("单词解释：" + result["simple_translation"])
print("美式音标： " + result["us-phonetic"])
print("详细解释： " + result["web_dict"])
pprint.pprint(result)