def deco(func):
    def wrap(*args):
        new_list = [abs(i) for i in args]
        # 3) new_list = map(abs, args)
        return func(*new_list)  # *args : unpacking
    return wrap

@deco
def mysum(x,y,z,k):
    return x+y+z+k

@deco
def mymultiply(x,y,z):
    return x*y*z

print(mysum(-1,-2,-3, -4))
print(mymultiply(-1,-2,-3))