class Emp:
    def setnum(self):
        self.setnum=40
        

    def display(self):
        print(self.setnum)

class Trainee(Emp):
    def setnum(self):
        self.setnum=45
    def resertnum(self):
        super().setnum()
obj1=Emp()
obj1.setnum()
print("number of working hour of emp:", end='')
obj1.display()

obj2=Trainee()
obj2.setnum()
print("number of working hour for trainee:", end=" ")
obj2.display()

obj2.resertnum()
print("Number of working hour has been resert:", end=" ")
obj2.display()
