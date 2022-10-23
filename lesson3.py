'''
class Student():
    amount_of_students = 0
    def __init__(self, height = 160):
        self.height = height
        Student.amount_of_students += 1
    def grow(self, height=1):
        self.height += height

Serhii = Student()
Oleg = Student(height=170)
print('Serhii - ', Serhii.height)
Serhii.grow(height=15)
print('Serhii - ', Serhii.height)
print('Oleg - ', Oleg.height)
'''

'''
class Student():
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am student. My name is {self.name}"
    def __del__(self):
        print('Training is over. I am now an expert')

serhii = Student(name='Serhii')
print(serhii)
'''

'''
class Student():
    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height

nick = Student(name='Nick')
john = Student(name='john')
print(nick.name)
print(bool(nick))
print(nick.__bool__())
print(len(nick))
print(nick.__len__())

print(john.name)
print(bool(john))
print(john.__bool__())
print(len(john))
print(john.__len__())
'''

class Car():
    def __init__(self, model=None, color=None, speed=150):
        self.model = model
        self.color = color
        self.speed = speed

mercedes = Car(model='mercedes')
mercedes = Car(color='gray')
print('model - ', mercedes.model)
print('color - ', mercedes.color)
print('speed - ',  mercedes.speed)
