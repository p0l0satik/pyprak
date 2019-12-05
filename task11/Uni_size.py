class siz():
    value = None
    def __get__(self, obj, cls):
        if self.value == None:
            if "__len__" in dir(obj):
                self.value = len(obj)
            else:
                self.value = int(obj)
        return self.value

def sizer(base_cl):
    class cl(base_cl): 
        size = siz()
    return cl
