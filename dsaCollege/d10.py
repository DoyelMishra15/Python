#OOPS

class Form:
    #x=10
    clg_name="dsaCollege"
    clg_mob=9999999999

    def __init__(self,name,p,a=18):
        self.name=name
        self.phone=p
        self.age=a
    
    def greet(self):
        print(f"Hello {self.name}, your age is {self.age}")

    def ucandoit(self):
        if self.age>=18:
            print(f"You can do it {self.name}!!")
        

o1 = Form("Aria","1234567890",20)
o2 = Form("Bob","0987654321")
print(o1.phone)
print(o2.age)

# o1.age=29
# print(o1.age)
# o2.age=1517
# print(o2.age)

o1.greet()
o2.ucandoit()
print(o1) #gives objects address

#what is adress of o2?? o2 is the address of itself

