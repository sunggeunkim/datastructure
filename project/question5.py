class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(ll, m):
    if ll == None:
        return None
    pre_runner = ll
    post_runner = ll
    n = m
    while n > 1:
        if pre_runner == None:
            return None
        pre_runner = pre_runner.next
        n -= 1
    while pre_runner.next:
        pre_runner = pre_runner.next
        post_runner = post_runner.next
    return post_runner.data


