import requests
def spider(sn):
    '''爬取当当网书籍'''
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
    #获取html内容
    html_data = requests.get(url).text

    #xpath对象

    selector = html.fromstring(html_data)

    #页面源代码