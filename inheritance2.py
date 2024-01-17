#1 class defination is one time process
class A():
    #2. constructor/esp.function
    def __init__(self,n):
        print(f'My name is {n}')
        pass
    pass
class B(A):
    #2. constructor/esp.defination
    def __init__(self,n):
        # We will call the parent constructor
        super().__init__(n)
        pass
    pass
class C(B):
    #2.constructor/esp.method
    def __init__(self,n):
        super().__init__(n)#call parent constructor
        pass
    pass

#2 create class external object is many time process
ceo1=C("Vishal")