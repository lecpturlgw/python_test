# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
# 只写了两个


class Dog:
    def eat(self):
        print('小狗爱啃骨头')

    def drink(self):
        print('小狗爱喝水')


dog = Dog()
dog.eat()
dog.drink()


# 定义一个类
class Person:
    def __init__(self, name, age, weight):
        # 实例熟悉 name age weigt
        self.name = name
        self.age = age
        self.weight =weight

    # run方法 传入time 大于60 体重减一，小于60 体重不变
    def run(self, time):
        if time > 60:
            self.weight -= 1
        elif time < 60:
            self.weight = self.weight
        return self.weight

    # eat方法
    def eat(self, food):
        if food == 'hanburger':
            self.weight += 1
        elif food == 'meat':
            self.weight += 1
        elif food == 'fruit':
            self.weight -= 0.5
        return self.weight

    # count方法，比较体重数值然后打印
    def count(self):
        if self.weight > 150:
            print(f'你太胖了，跑步减肥吧！你现在的体重是{self.weight}')
        elif self.weight < 90:
            print(f'你太瘦了，多吃点！你现在的体重是{self.weight}')
        else:
            print(f'标准体重！你现在的体重是{self.weight}')


name = 'liu'
age = 21
weight = 145
person = Person(name, age, weight)
person.eat('fruit')
person.run(20)
person.count()

