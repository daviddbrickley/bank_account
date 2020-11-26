class Person:
    def __init__(self,firstname):
        self.name = firstname


    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Shwetanshu')
p.say_hi()

David = Person('Brickley')
David.say_hi()

Emmanuel = Person('Torbor')
Emmanuel.say_hi()
