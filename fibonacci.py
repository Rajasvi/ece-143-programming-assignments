def fibonacci(n):
    ''' This generator func computes the first n Fibonnacci numbers.'''
    assert n>=0
    assert isinstance(n, int)
    a = 1
    b = 1
    if n==0:
        yield a
    for i in range(1,n+1):
        if i==1 or i==0:
            yield a
        elif i==2:
            yield b
        else:
            c = a+b
            yield c
            a,b=b,c