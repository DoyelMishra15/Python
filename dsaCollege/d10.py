#OOPS

class Form:
    #x=10
    clg_name="dsaCollege"
    clg_mob=9999999999

    def __init__(self,name,p,a=18):
        self.name=name
        self.phone=p
        self.age=a
        

o1 = Form("Aria","1234567890",20)
o2 = Form("Bob","0987654321")
print(o1.phone)
print(o2.age)

o1.age=29
print(o1.age)