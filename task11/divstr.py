class DivStr(str):
    def __init__(self, *args): 
        super().__init__()
    st = ""
    no = ("__class__", "__new__", "__getattribute__", "__getattr__", "__repr__", "__str__")
    for s in str.__dict__.keys():
        if s not in no and callable(str.__dict__[s]):  
            st += "def {0}(self, *args, **kwargs): return (type(self))(super(DivStr, self).{0}(*args, **kwargs)) \n".format(s) 
    exec(st)

    def __truediv__(self, other):
        s = str(self)
        return type(self)(s[:len(s) // other])

    def __len__(self):
        return len(str(self))
