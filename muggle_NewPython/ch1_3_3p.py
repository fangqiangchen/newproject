import urge

cat1 = "https://http.cat/200"
cat2 = "https://http.cat/300"
cat3 = "https://http.cat/404"

urge.web_screenshot(cat1).once()
urge.web_screenshot(cat2).once()
urge.web_screenshot(cat3).once()