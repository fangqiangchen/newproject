# 导入库
import urge

url = "http://www.bing.com"
example = "http://www.example.com"

urge.web_screenshot(url).once()

urge.web_screenshot(example).every(5)

urge.start()