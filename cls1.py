
class Calculater:

    num=100  #class variable

    def Getdata(self):
        print('i am now executing as method in class')
    # def __init__(self):
    #     print("i'm called automatically")

    def __init__(self,a,b):
        self.firstNum=a
        self.secondNum=b
        print("i will come frist")

    def summtion(self):
        return self.firstNum+self.secondNum+Calculater.num

obj=Calculater(50,35)
obj.Getdata()
print(obj.num)
print(obj.summtion())
