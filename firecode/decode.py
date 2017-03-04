class treeNode:
    def __init__(self, value = "", rest = ""):
        self.value = value
        self.rest = rest
    
def is_in_code(x):
    return (x[0] != "0" and int(x) < 27 and int(x) > 0)
    
def decode_string(msg):
    if msg == None:
        return None
    if len(msg) == 0:
        return 0
    if len(msg) == 1:
        if int(msg[0]) > 0:
            return 1
        else:
            return 0
    q = []
    valid = 0
    if is_in_code(msg[0]):
        q.append(treeNode(msg[0], msg[1:]))
    if len(msg) > 1 and is_in_code(msg[:2]):
        q.append(treeNode(msg[:2], msg[2:]))
    while len(q) > 0:
        node = q.pop(0)
        if is_in_code(node.value):
            if node.rest == "":
                valid += 1
            if len(node.rest) > 0 and is_in_code(node.rest[0]):
                q.append(treeNode(node.rest[0], node.rest[1:]))
            if len(node.rest) > 1 and is_in_code(node.rest[:2]):
                q.append(treeNode(node.rest[:2], node.rest[2:]))
    return valid

print(decode_string("113021"))
print(decode_string("2202"))
print(decode_string("29"))
print(decode_string("521"))
