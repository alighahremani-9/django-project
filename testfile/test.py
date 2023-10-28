class main:
    def __init__(self,name):
        self.name= name
        

    def __str__(self):
        return f"name1:{self.name}"
    
    
    def get_age(self):
        return f"age_1=18"
    

class second(main):
    def __init__(self, name , id=1):
        super().__init__(name)
        super().get_age()
        self.get_age()
        self.id=id
    
    def __str__(self):
        return f"name2:{self.name}\nid:{self.id}"
    
    def get_age(self):
        return f"age_2=15"
    

p1= main("ali")
p2= second("mohammad",3)

print(p1)
print(p2)
print(p1.get_age())
print(p2.get_age())
