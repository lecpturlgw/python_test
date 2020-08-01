'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''


# 定义一个天山童姥类
class TongLao:
    # 构造方法 定义两个属性：血量和武力值
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    # see_people方法，传入name
    def see_people(self, name):
        # 判断name的值进行打印
        if name == 'WYZ':
            print('师弟！！！！')
        elif name == 'LQS':
            print('呸，贱人')
        elif name == 'DCQ':
            print('叛徒！我杀了你')

    # flight_zms方法，传入敌人血量和敌人武力值
    def flight_zms(self, enemy_hp, enemy_power):
        # 调用flight_zms方法后，自身的血量缩减两倍，武力值增强10倍
        self.hp = int(self.hp)/2
        self.power = int(self.power)*10
        enemy_hp = enemy_hp - self.power
        my_hp = self.hp - enemy_power
        # 判断自己的血量和敌人血量大小
        if my_hp > enemy_hp:
            print('你输了！')
        elif my_hp < enemy_hp:
            print('我输了！')
        else:
            print('平局')


if __name__ == '__main__':
    my_hp = int(input('请输入我的血量：'))
    my_power = int(input('请输入我的武力值：'))
    enemy_hp = int(input('请输入敌人的血量：'))
    enemy_power = int(input('请输入敌人的武力值：'))
    name = input('请输入（WYZ/LQS/DCQ：）')
    # 实例化TongLao类，并传入my_hp，my_power
    tonglao = TongLao(my_hp, my_power)
    # 调用see_people方法，并传入name
    tonglao.see_people(name)
    # 调用flight_zms方法并传入enemy_hp，enemy_power
    tonglao.flight_zms(enemy_hp, enemy_power)


