def decorator(func):
    def result(*args):
        sum_result = 0
        for i in args:
            i = abs(i)
            sum_result += i
        return sum_result
    return result


@decorator
def mysum(x,y,z,k):
    return x+y+z+k

#mysum = decorator(mysum)
print(mysum(1,2,3,-4))