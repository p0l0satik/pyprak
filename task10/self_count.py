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
        WeAre._count -= 1
    
    def __del__(self):
        WeAre._count -= 1
# a = WeAre()
# print(a.count)
# b, c = WeAre(), WeAre(),
# a.count = 100500
# print(a.count, b.count, c.count)
# del b.count
# del b
# print(a.count)
# b, c = WeAre(), WeAre(),
# a.count = 100500
# print(a.count, b.count, c.count)
# del b.count
# del b
# print(a.count)
a, b = WeAre(), WeAre()
a.count = -1
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del a
a, b = WeAre(), WeAre()
del b.count
del a
print(b.count)