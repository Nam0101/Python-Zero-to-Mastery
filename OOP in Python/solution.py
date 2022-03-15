from random import choice


class student:
    def __init__(self,name,age=0):
        self.name = name
        self.age = age
    
    def greeting(self):
        _greeting =[
            "hi, my name is " + self.name,
            "I'm " + str(self.age) + " years old"
        ]
        greeting=choice(_greeting)
        return greeting.format(self.name)

def clas_create(student_name):
    return [Student(name) for name in student_name]

if __name__ == "__main__":
    names = ["Alice","Bob","Charlie","David","Eve","Frank","Grace","Heidi","Iris","Jack","Karen","Linda","Molly","Nancy","Oscar","Penny","Quinn","Rachel","Samantha","Tina","Ursula","Victor","Wendy","Xavier","Yvonne","Zoey"]

    for student in names:
        print(student.greeting())