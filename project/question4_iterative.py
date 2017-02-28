def question4_iterative(T, r, n1, n2):
  while True:
    if (r < n1 and r < n2):
        right_child = None
        for right_child_candidate_index in range(r+1, len(T[r])-1):
            if T[r][right_child_candidate_index] > 0:
                right_child = right_child_candidate_index
                break     
        if right_child == None:
            return "No least common ancestor"     
        r = right_child
    elif (r > n1 and r > n2):
        left_child = None
        for left_child_candidate_index in range(0,r-1):
            if T[r][left_child_candidate_index] > 0:
                left_child = left_child_candidate_index
                break            
        if left_child == None:
            return "No least common ancestor" 
        r = left_child
    else:      
        return r


        







