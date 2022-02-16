def fast_mul(x,y):
    a=x
    b=y
    sum = 0
    while (x>=1):
        if (x%2!=0):
            sum+=y
        x//=2
        y*=2
    assert (sum == (a * b))
    return sum
print(fast_mul(2, 2))

def fast_pow(x,y):
    assert (not ((x==0) and (y==0)))
    a = x
    b = y
    sum = 0
    if(y==0):
        return 1
    if(y==1 or x==1):
        return x
    while(y>1):
        sum+=fast_mul(x,x)
        y-=1
    assert (sum == (a ** b))
    return sum
print(fast_pow(0,1))