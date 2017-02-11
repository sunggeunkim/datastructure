def question1(s, t):
    if t == "":
        return True
    for c in t:
        if c not in s:
            return False
        
        

question1("udacity", "adu")
