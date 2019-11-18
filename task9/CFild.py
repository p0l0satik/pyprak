def fcounter(clas, *args):
    ex = clas(*args)
    cm, cf, om, of = [], [], [], []
    for el in dir(clas):
        if "_" !=  el[0]:
            if callable(getattr(clas, el)):
                cm.append(el)
            else:
                cf.append(el)
    for el in dir(ex):
        if "_" !=  el[0]:
            if callable(getattr(ex, el)):
                if el not in cm:
                    om.append(el)
            else:
                if el not in cf:
                    of.append(el)
    return sorted(cm), sorted(cf), sorted(om), sorted(of)

