# 模块化，导入TongLao类
from Game.TSTL.tl import TongLao


# 定义一个Xuzhu类，继承TongLao类
class Xuzhu(TongLao):
    # 构造方法，实例化时不用传值
    def __init__(self):
        pass

    # 定义一个read方法
    def read(self):
        print('罪过罪过')


if __name__ == '__main__':
    # 实例化
    xuzhu = Xuzhu()
    # 调用read方法
    xuzhu.read()