def deco(func):
    new_list = []
    def wrap(*args):
        for arg in args:
            arg = abs(arg)
            new_list.append(arg)
        new_tuple = tuple(new_list)
        return func(*new_tuple)
    return wrap

@deco
def mysum(x,y,z,k):
    return x+y+z+k

@deco
def mymultiply(x,y,z):
    return x*y*z

print(mysum(-1,-2,-3, -4))
print(mymultiply(-1,-2,-3))