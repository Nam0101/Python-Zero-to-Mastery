class Toy(object):
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.myDict = {
            'name': "Nam",
            "age": self.age,
            "color": self.color
        }

    def __str__(self):
        return self.color

    def __call__(self):
        print('hello world')

    def __getitem__(self, i):
        return self.myDict[i]


myToy = Toy("red", 100)
print(str(myToy))
myToy()
print(myToy['name'])
