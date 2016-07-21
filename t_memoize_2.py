import time

def decorator(func):
    cached = {}
    def result(x,y):
        key = (x,y)
        if key not in cached:
            time.sleep(1)
            cached[key] = func(x,y)
        return cached[key]
    return result

@decorator
def mysum(x,y):
    return x+y

@decorator
def mymultiply(x,y):
    return x*y

print(mysum(3,5)) #8
print(mysum(4,6)) #10
print(mysum(3,5))

print(mymultiply(2,5)) #10
print(mymultiply(3,5)) #15
print(mymultiply(2,5))