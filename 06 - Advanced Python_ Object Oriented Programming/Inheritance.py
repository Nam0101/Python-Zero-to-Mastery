
class User(object):
    def __init__(self, email):
        self.email = email

    def log_in(self):
        print("Loged in")

    def attacks(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, username, power):
        self.username = username
        self.power = power

    def attacks(self):
        User.attacks(self)
        print(f'Attacking with {self.power} ...')


class Archer(User):
    def __init__(self, username, rows, email):
        super().__init__(email)
        self.username = username
        self.rows = rows

    def attacks(self):
        User.attacks(self)
        print(f'Attacking with {self.rows} ...')


Archer1 = Archer('Nam', 100, 'nam@gmail.com')
Archer1.log_in()
Archer1.attacks()
print(Archer1.email)
print(isinstance(Archer1, Archer))
print(isinstance(Archer1, object))
print(dir(Archer1))
