# OOP
class player:
    # Class Object Attribute
    memberships = True

    def __init__(self, name, age):
        if player.memberships:
            self._name = name
            self._age = age

    def shout(self):
        print(f'my name is {self._name}')

    def run(self, hello):
        print(f'{hello} my name is {self._name}')

    @classmethod
    def add_things(cls, num1, num2):
        return cls('Teddy', num1+num2)

    @staticmethod
    def add_things(num1, num2):
        return num1+num2


#player1 = player("nam", 20)
#player2 = player("Nhan", 21)
#print(player1.name, player1.age)
# printplayer1.shout()
# player1.run("hello")
player3 = player.add_things(2, 3)

print(player3)
