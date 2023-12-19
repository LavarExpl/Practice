class wiz:
    def __init__(self,name):
        if not name:
         raise ValueError('Error raised')
        self.name = name
        ...
        
class Student(wiz):
    def __init__(self,name,house):
        
        super().__init__(name)
        self.house = house
        ...


class Prof(wiz):
    
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

wz =wiz('rec')
student= Student('lavar','larry')
p = Prof('shot','defense')

