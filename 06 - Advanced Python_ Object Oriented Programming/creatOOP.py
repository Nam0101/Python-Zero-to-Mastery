# OOP
class player:
    # Class Object Attribute
    memberships = True

    def __init__(self, name, age):
        if player.memberships:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'{hello} my name is {self.name}')


player1 = player("nam", 20)
player2 = player("Nhan", 21)
print(player1.name, player1.age)
player1.shout()
player1.run("hello")