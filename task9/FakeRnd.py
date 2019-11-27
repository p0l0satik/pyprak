Time = -1
def randint(a, b):
    global Time
    Time += 1
    return a if Time % 2 == 0 else b

# - I am a great winter Warg.
# - What makes you so great?
# - I drink wodka!

Warg, l, now = [], 0, 0 
def randrange(*args):
    global Warg, now, l
    nl = len(args)
    if nl == 4: nl = 3
    print(Warg)
    if l == nl and tuple(Warg[:l]) == args[:l] or (l == 1 and Warg[1] == args[0]):
        now += Warg[2]
        if Warg[2] > 0 and now % Warg[1] > Warg[0]:
            now = Warg[0] + (now + Warg[2]) % Warg[1]
        elif Warg[2] < 0 and  now <= Warg[1]:
            now = Warg[0] + (-Warg[1] + now) 
        return now 
    else:
        Warg = [0, 0, 1]
        if len(args) == 1:
            Warg[1] = args[0]
            now, l = 0, nl
        else:
            Warg[:nl] = args[:nl]
            now, l = args[0], nl
        return now

