s = input()
gl = {}
while s:
    
    if s == ".": break
    if s[0] == "#": 
        s = input()
        continue
    if "=" in s:
        try:
            ident = s[:s.find("=")]
            exec(s, gl)
        except Exception:
            if not ident.isidentifier():
                print("invalid identifier '{0}'".format(ident))
            else:
                print("invalid assignment '{0}'".format(s))
    else:
        try:
            print(eval(s, gl))
        except Exception as ERR: 
            print(ERR)
    s = input()
