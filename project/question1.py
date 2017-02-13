def increment_count(s, s_dict):
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1

def question1(s, t):
    if s == None or t == None:
        return None
    if t == "":
        return True
    s_dict = {}
    t_dict = {}
    for i in range(len(t)):
        increment_count(s[i], s_dict)
        increment_count(t[i], t_dict)
    
    i = 0
    while True:
        match = True
        for j in range(len(t)):
            if t[j] not in s_dict or s_dict[t[j]] != t_dict[t[j]]:
                match = False
                break
        if match == True:
            return True
        if i + len(t) >= len(s):
            return False
        else:
            s_dict[s[i]] -= 1
            increment_count(s[i+len(t)], s_dict)
            i += 1
