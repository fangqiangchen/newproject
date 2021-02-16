def format_str():

    name = 'zhangsan'
    print('Welcome，%s '% name)
    #zhengxing ，floatleixing
    num = 12.33
    print('your input:%.4f' % num)

    num2 = 54
    print('your number is %04d' % num2)
    #
    t = (1,2,3,4)
    print('your input tuble is %s' % str(t))

    print('your name is:%(name)s' % {'name':name})

def format_str2():

    print('welcome,{0},{1},---{1}'.format('zhangsan','no time no see'))
    #使用名称
    print('hello,{username},your number is {num}'.format(username='zangshan',num=45))
    #格式化元组
    point = (1,0)
    print("zuobiao:{0[0]}:{0[1]}".format(point))
    #格式化类
    user = User('李四',23)
    # print(user.show())
    print(user)
class User(object):

        def __init__(self, username, age):

            self.username = username
            self.age = age
        def show(self):
            return '用户名:{self.username},年龄：{self.age}'.format(self=self)

        def __str__(self):
            return  self.show()

if __name__ == '__main__':
    format_str()
    format_str2()