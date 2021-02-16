import requests
def get_book():
    """获取书本信息"""
    # url = 'http://search.dangdang.com/'

    # rest = requests.get(url,params={
    #     'key': 'python',
    #     'act': 'input'
    # })
    url = 'http://search.dangdang.com/?key=python&act=input'
    rest = requests.get(url)
    print(rest.text)
    #http状态码
    print(rest.status_code)
    #网页编码
    print(rest.encoding)

if __name__ == '__main__':
    get_book()