def mean(this_list):
    '''
    Takes a list of number and returns the mean
    '''
    
    if len(this_list) <= 0:
        return "You passed an empty list"
    
    list_example = [1.0,2.0]
    
    if type(this_list) != type(list_example):
        return "You didn't pass a list"
    
    total=0
    for item in this_list:
        total = total + item
    return total/len(this_list)