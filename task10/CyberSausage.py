class sausage():
    ## OK NOW I AM HUNGRY!!!
    def __init__(self, mince = "pork!", volume = 1):
        self.mince = mince
        self.size = eval(str(volume)) * 12
        if len(mince) > 12:
            self.mince_str = mince[:12]
        else:
            self.mince_str = mince * (12 // len(mince)) + mince[:12 % len(mince)]
    
    def __str__(self):
        blocks =  int(self.size) // 12
        left = int(self.size) % 12
        up = "/------------\\" * blocks  
        down = "\\------------/" * blocks 
        s = "|" +  self.mince_str + "|"
        body = s * blocks 
        if left:
            body += s[:left + 1] + "|"
            up += "/------------"[:left +1] + "|"
            down += "\\------------"[:left + 1] + "|"
        if int(self.size) == 0:
            up = "/|"
            down = "\\|"
            body = "||"
        return "\n".join((up, body, body, body, down))

    def __truediv__(self, num):
        return sausage(self.mince, (self.size / num) / 12)
    
    def __mul__(self, num):
        return sausage(self.mince, (self.size * num) / 12)

    def __add__(self, other):
        return sausage(self.mince, (self.size + other.size) / 12)
    
    
    def __sub__(self, other):
        size = (self.size - other.size) / 12
        if size < 0:
            size = 0
        return sausage(self.mince, size)
    
    def __bool__(self):
        return bool(self.size)
    __rmul__ = __mul__
