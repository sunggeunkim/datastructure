class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1
    
    def __init__(self,lower_bound,upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
 
    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"

def print_list(a):
    for r in a:
        print(r)


def insert_and_merge(input_range_list,new_range):
    if input_range_list == None or len(input_range_list) == 0:
        return new_range
    if new_range == None:
        return input_range_list
    if new_range.lower_bound <= input_range_list[0].lower_bound:
        new_input_range_list = [new_range] + input_range_list
    elif new_range.lower_bound >= input_range_list[-1].lower_bound:
        new_input_range_list = input_range_list + [new_range]
    else:
        for i in range(len(input_range_list)-1):
            if input_range_list[i].lower_bound <= new_range.lower_bound and \
               input_range_list[i+1].lower_bound >= new_range.lower_bound:
                new_input_range_list = input_range_list[:i+1] + [new_range] + input_range_list[i+1:]
    merged_list = [new_input_range_list[0]]
    import pdb;pdb.set_trace()
    for i in range(1,len(input_range_list)):
        last_merged = merged_list[-1]
        not_merged_yet = new_input_range_list[i]
        if not_merged_yet.upper_bound > last_merged.upper_bound:
            if not_merged_yet.lower_bound <= last_merged.upper_bound:
                last_merged.upper_bound = not_merged_yet.upper_bound
            else:
                merged_list.append(not_merged_yet)
    return merged_list

merged = insert_and_merge([Range(1,10), Range(5,8), Range(8,15)], Range(0,5))
print_list(merged)
