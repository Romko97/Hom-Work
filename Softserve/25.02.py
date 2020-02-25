from random import randint
class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides=number_of_sides
        self.sides=[0 for i in range(number_of_sides)]
    

    def ImputSides(self):
        self.sides=[float(input("Enter sides"+str(i+1)+":"))for i in range(self.number_of_sides)]

    def DispSidef(self):
        for i in range(self.number_of_sides):
            print("Side", i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)  #super().__init__(3) 

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Scver(Polygon):
    def __init__(self):
        Polygon.__init__(self,2)  #super().__init__(3) 

    def findArea(self):
        a, b = self.sides
        S = a*b
        print('The area of the triangle is %0.2f' %S)

'''
t = Triangle()
t.ImputSides()
t.DispSidef()
t.findArea()
 '''
''' 
s = Scver()
s.ImputSides()
s.findArea()
'''

# 1.  Створити клас машина з атрибутами name,  make, model та методами
# start та stop, які виводять інформацію про те що автомобіль стартував чи
# зупинився відповідно.

class Car():

    def __init__(self, name="?",  make="?", color="?"):
        self.name = name
        self.make = make
        self.color = color
    
    def __repr__(self):
        return self.name, self.make, self.color

    def start(self):
        print(self.name, " почав їхати")

    def stop(self):
        print(self.name," зупинився")


car1 = Car('Mersedes',"German","red")
car2 = Car('Mitsubishi','Japanese','bloo')
'''
car1.start()
car2.stop()
'''

# 2.  Створити клас особа,  в якому конструктор встановлює ім’я,
# а метод info виводить повідомлення “Hello, my name is
# {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль, 
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
# {ім’я конкретного екземпляра класу}  moves at the speed
# {speed(цей параметр метод moveотримує як вхідний)} km / h

class Person:
    def __init__(self, name,):
        self.name = name
    
    def info(self):
        print("“Hello, my name is", self.name)

class Auto:
    def __init__(self, name,):
        self.name = name
    
    def move(self, speed):
        print(f"{self.name} moves at the speed {speed} km/h")

n = ["Максим", "Матвій", "Давид", "Артем", "Олександр"]
a = ['Alfa Romeo', 'Autobianchi', 'Cizeta', 'De Tomaso', 
    'DR Motor', 'Ferrari', 'Fiat', 'Intermeccanica', 'Lamborghini',
    'Lancia', 'Maserati', 'Pagani', 'Siata', 'Vignale']
for person in range(len(n)):
    person = Person(n[person])
    person.info()
for car in range(len(a)):
    car = Auto(a[car])
    car.move(randint(10, 300))
