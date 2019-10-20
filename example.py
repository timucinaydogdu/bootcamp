def make_list_in_range(x,y):
    
    new_list=[]
    for a in range(x+1,y):
        new_list.append(a)
    
    return new_list

def make_list_of_even(x,y):
    
    new_list=[]
    for a in range(x+1,y):
        if a%2==0:
            new_list.append(a)
    
    return new_list
