'''
题目：
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''


# 设定初始值玩法
def flight():
    # 定义四个变量
    # 我的初始血量为1000，攻击力为200
    hp = 1000
    power = 200
    # 敌人的初始血量为1000，攻击力为190
    enemy_hp = 1000
    enemy_power = 200
    # 我的生命值=初始生命值-敌人的攻击力，谁的值先为0谁输，如果我的生命值和敌人生命值相等且小于等于0，那么为平局
    while True:
        hp = hp - enemy_power
        enemy_hp = enemy_hp - power
        if hp == enemy_hp <= 0:
            print('平局')
            break
        elif hp <= 0:
            print('我输了')
            break
        elif enemy_hp <= 0:
            print('你输了')
            break

# 调用flight函数
flight()


# # 自定义血量与攻击力
# def game():
#     # 自定义设置生命值和攻击力
#     hp = int(input('请输入你的生命值：'))
#     power = int(input('请输入你的攻击力：'))
#     enemy_hp = int(input('请输入敌人的生命值：'))
#     enemy_power = int(input('请输入敌人的攻击力：'))
#     while True:
#         hp = hp - enemy_power
#         enemy_hp = enemy_hp - power
#         if hp == enemy_hp == 0:
#             print('平局')
#             break
#         elif hp <= 0:
#             print('我输了')
#             break
#         elif enemy_hp <= 0:
#             print('你输了')
#             break
#
#
# game()

