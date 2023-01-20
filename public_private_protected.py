class exam_1():
    def public_func(self):
        print("I am Public and open to the world!")
    def _protected(self):
        print("I am protected from out side except my drive class!")
    
    def __protected(self):
        print("I am private. I wont response to the out side of the class. Fuck off babes!")
    
    def access_private(self):
        self.__protected()
        
class exam_2(exam_1):
    def __init__(self):
        self._protected()
        self.access_private()
        self.public_func()
        
obj = exam_2()