
def no_repeat(param : list) :#{
    if not param : return "invalid list"
    for i in param :
        if param.count(i) == 1 : return i;

result = no_repeat([4, 5, 1, 2, 0, 4, 1, 0])
print(result)