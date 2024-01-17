class Animal():
    #1. property/variable
    name=""
    #2. constructor/esp.method
    def __init__(self,n):
        self.name=n
        pass
    pass
class Dog(Animal):
    #2. constructor/esp.function
    def __init__(self,n):
        #call the parent constructor
        super().__init__(n)

        pass
    pass
dog1=Dog("Shera")
print(F'My dog name is {dog1.name}')