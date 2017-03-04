# Collections module has already been imported.
class IpNode:
    def __init__(self, value=[], front=[], back="", level=0):
        self.value = value
        self.front = front
        self.back = back
        self.level = level
        
    
def generate_ip_address(input):          
    # Return type should be a List.
    '''
    "19216810"
    "1", front=[], back="9216810", level=1
    back_length = 7
    1,2,3
    back[:1]="9", front = ["1"], back="216810", level=2
    back[:2]="92", front = ["1"], back="16810", level=2
    '''
    if input == None or len(input)<4:
        return None
    ip_list = []
    #import pdb;pdb.set_trace()
    for j in range(1,4):
        firstNode = IpNode(value=input[:j], front=[], back=input[j:], level=1)
        q = []
        q.append(firstNode)
        while len(q) > 0:
            currentNode = q.pop(0)
            back = currentNode.back
            front = currentNode.front
            value = currentNode.value
            level = currentNode.level
            back_length = len(back)
            front.append(value)
            if level == 4 and back_length==0:
                ip_list.append('.'.join(front))
            elif back_length >= 4-level:
                for i in range(1,min(4, back_length+1)):
                    if int(back[:i]) <= 255:
                        newNode = IpNode(value=back[:i], front=list(front), back=back[i:], level=level+1)
                        q.append(newNode)
            
    return ip_list


print(generate_ip_address("2551025510"))
