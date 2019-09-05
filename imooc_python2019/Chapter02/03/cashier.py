print('欢迎使用收银台程序')

goodz = input('请输入商品名称：')
price = input('请输入商品单价：')
num = input('请输入商品数量：')

total = int(price) * int(num) * 0.9

alipay_total = total*0.95

print('你购买的商品为：')
print(goodz)
print('商品的总价为')
print(total)
print('您需要使用支付宝支付')
print(alipay_total)