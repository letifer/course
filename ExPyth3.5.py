def my_map(x,y,z):
    res_list = [x(i,l) for i,l in zip(y,z)]
    return res_list
def my_filter(a,c):
    res_list = [x for x in c if a(x)]
    return res_list
