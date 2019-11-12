def turtle(coord, direction):
    cord = list(coord)
    direct = direction
    order = yield cord 
    while order:
        if order == "f":
            cord[direct % 2] += 1 if direct < 2 else -1 
        elif order == "l":
            direct += 1
        else:
            direct -= 1
        direct %= 4    
        order = yield cord
