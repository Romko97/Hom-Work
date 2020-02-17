def flatten(a_list, flat_list=None):
    if flat_list is None:
        flat_list = []
    
    for i in a_list:
        if isinstance(i, list):
            flatten(i, flat_list)
        else:
            flat_list.append(i)
    return flat_list

a = [1,2,3,[3,2,1],2]
x = flatten(a)
print(x)