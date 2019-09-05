a ='abc'

b = 1
c = '123'
d = ['a','b','c','d']
e = 1.513414
f = input('请输入F的值：')
print(type(b))
print(type(str(b)))
print(type(int(c)))
print(len(d))
print(type(e))
print(e,4)
print(f)

def trapezoid_area(base_up,base_down,height):
    area = (base_up+base_down)*height/2
    print(area)
    