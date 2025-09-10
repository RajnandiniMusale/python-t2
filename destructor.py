

class student():
    def __init__(self,name):
        print("constructor is called")
        self.name=name

    def show(self):
        print("name:",self.name)

    def __del__(self):
        print("destructor is called...object is deleted")


        #object creation
s1=student("rajnandini")
s1.show()

del s1
print("end of program")