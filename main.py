class information:

  def __init__(self,name,age):
    self.name = name
    self.age = age
  def info(self):
    print(f"the {self.name} is {self.age} year old") 
a=information("harry",20)
b=information("neetu",22)
b.name = "kuldeep"
a.info()
b.info()

class marks:
  name = "kuldeep"
  sem  = 7.21
  sem2 = 6.62
a = marks()
print("the marks of" ,a.name,"in sem 1st is",a.sem,"and 2nd sem is",a.sem2)

class clgmarks:
 def __init__(self,name,sem1,sem2):
  self.name = name
  self.sem1 = sem1
  self.sem2 = sem2

 def info(self):
   print(f"the marks of {self.name} in sem 1st is {self.sem1} and in 2nd sem is {self.sem2} it is complete infomation ")  

a = clgmarks("kuldeep",7.21,6.34)
a.info()



class myclass:
  @staticmethod
  def add(x,y):
    return x+y
result = myclass.add(6,4)
print(result)

