
def increment_count(s, s_dict):
        if s in s_dict:
            s_dict[s] += 1
        else:
            s_dict[s] = 1

def question1(s, t):
    if t == "":
        return True
    s_dict = {}
    t_dict = {}
    for i in range(len(t)):
        increment_count(s[i], s_dict)
        increment_count(t[i], t_dict)
    
    i = 0
    while True:
        for j in range(len(t)):
            if s_dict[s[j]] != t_dict[t[j]]:
                break
        if j == len(t)-1:
            return True
        if i + len(t) < len(s):
            break
        else:
            t_dict[t[i]] -= 1
            t_dict[t[i + len(t)] += 1
            i += 1
            
            
        

question1("udacity", "adu")
