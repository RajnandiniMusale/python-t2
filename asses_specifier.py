class Student():
    def __init__(self,name,age,grade):
        self.name=name                       # for public asses specifier we not use any symbol
        self._age=age                        # for protected we use a single _ 
        self.__grade=grade                    # for private we use a double __
   
   
    def display(self):
        print("name:",self.name)
        print("age",self._age)
        print("grade:",self.__grade)


s1=Student("Rajnandini",20,"A")
print("public:",s1.name)
print("protected:",s1._age)
print("grade:",s1._Student__grade)      # we can not asses private member directily so we use _classname.__variablename

s1.display()