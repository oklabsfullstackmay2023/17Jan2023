class A():
    #2. Constructor
    def __init__(self,n):
        print(f"My name is {n}")
        pass
    pass
class B(A):

    #2. Constructor
    def __init__(self,n):
        # We will call the parent constuctor
        super().__init__(n)
        pass
    pass


ceo1= B('Anil')