class morse():
    def __init__(self, s = "di dit dah"):
        self.res = []
        self.fl = False
        
        if " " in s:
            self.alf = s.split(" ")
            if len(self.alf) == 2:
                self.alf.append(self.alf[0])
                self.alf.append(".")
            elif len(self.alf) == 3:
                self.alf[1], self.alf[2] = self.alf[2], self.alf[1]
                self.alf.append(".")
            elif len(self.alf) == 4:
                self.alf[1], self.alf[2] = self.alf[2], self.alf[1]
            self.alf.append(" ")
            self.alf.append(", ")
        elif len(s):
            self.alf = list(s) 
            if len(self.alf) == 2:
                self.alf.append(self.alf[0])
                self.alf.append("")
            elif len(self.alf) == 3:
                self.alf[1], self.alf[2] = self.alf[2], self.alf[1]
                self.alf.append("")
            elif len(self.alf) == 4:
                self.alf[1], self.alf[2] = self.alf[2], self.alf[1]
            self.alf.append("")
            self.alf.append(" ")
        self.res.append(self.alf[3])

    def __str__(self):
        return "".join(list(reversed(self.res)))

    def __pos__(self):
        if len(self.res) > 1 and self.res[-1] != self.alf[5]:
            self.res.append(self.alf[4])
        if self.fl:
            self.res.append(self.alf[0])
        else:
            self.res.append(self.alf[2])
        self.fl = True
        return self

    def __neg__(self):
        self.fl = True
        if len(self.res) > 1 and self.res[-1] != self.alf[5]:
            self.res.append(self.alf[4])
        self.res.append(self.alf[1])
        return self

    def __invert__(self):
        self.fl = False
        self.res.append(self.alf[5])
        return self
