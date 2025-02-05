class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person sınıfı türetildi.")

    def intro(self):
        print(self.name,self.surname,self.age)
class Student (Person):
    pass

class Teacher(Person):
    pass
p1=Person("Mustafa Emir","Ata",20)
p1.intro()

s1=Student("Mehmet Eymen","Ata",12)
s1.intro()

t1=Teacher("Sadık","Turan",40)
t1.intro()

