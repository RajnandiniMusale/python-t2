class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display(self):
        print("my name is:",self.name)
        print("my currently age is:",self.age)

s1=Student("Rajnandini",20)
s1.display()