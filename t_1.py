import time

cached_1 = {}

def mysum(x,y):
    key = (x,y)
    if key not in cached_1:
        time.sleep(1)
        cached_1[key] = x+y
    return cached_1[key]


cached_2 = {}

def mymultiply(x,y):
    key = (x,y)
    if key not in cached_2:
        time.sleep(1)
        cached_2[key] = x*y
    return cached_2[key]

print(mysum(3,5)) #8
print(mysum(4,6)) #10
print(mysum(3,5))

print(mymultiply(2,5)) #10
print(mymultiply(3,5)) #15
print(mymultiply(2,5))
