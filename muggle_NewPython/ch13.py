import os
import urge

os.environ["APP_KEY"] = "2402e28def14849b"
os.environ["APP_SECRET"] = "r6MzkjgYV5aIVlVosycGi0M7y6czlSCx"

result = urge.translate("hello").once()

print(result)