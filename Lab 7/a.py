class A(object):
    
    def __init__(self, b):
        self.b = b
    
    def method_a1(self):
        self.b = 5
        pass

    def __eq__(self, other):
        return False

    def __hash__(self):
        return hash(self.b)
