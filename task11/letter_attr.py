class LetterAttr():
    def __setattr__(self, name, value = ""):
        val = value
        for s in val:
            if s not in name:
                val = val.replace(s, "")
        object.__setattr__(self, name, val)


    def __getattr__(self, name):
        object.__setattr__(self, name, name)
        return name

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)
    