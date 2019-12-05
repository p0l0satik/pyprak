class WeAre():
    fl = False
    _count = 0
    def __init__(self):
        WeAre.fl = True
        WeAre._count += 1
        WeAre.fl = False

    @property
    def count(self):
        return WeAre._count
    
    @count.setter
    def count(self, value):
        if WeAre.fl:
            print("SAS")
            WeAre._count += value

    @count.deleter
    def count(self):
        pass
        # WeAre._count -= 1
    
    def __del__(self):
        WeAre._count -= 1
