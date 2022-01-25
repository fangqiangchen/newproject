import urge
import os
import pprint

os.environ["YOUDAO_AI_KEY"] = "2402e28def14849b"
os.environ["YOUDAO_AI_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"


word = ' scissor '
res = urge.translate(word,full=True).once()
pprint.pprint(res)
for i in res['wfs']:
    print(word + "的 " +i["wf"]['name']+"是" + i["wf"]["value"])

# print("详细解释： " + result["web_dict"])
