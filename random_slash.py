import numpy as np
import random

def gen_rand_slash(m=6,n=6,direction='back'):
    ''' This function creates a random pixel slash from random pixel 
    in given direction.

    :m: number of rows in image.
    :n: number of columns in image.
    :direction: direction in which you want to generate the random slash.

    '''
    assert isinstance(direction,str)
    assert direction == 'back' or direction == 'forward'
    assert m>=2 and n>=2

    x = np.zeros((m,n))
    xi,xj = 0,0
    
    while True:
        xi,xj = random.randint(0,m-1),random.randint(0,n-1)
        if direction == "back" and (xi==0 or xj==0):
            continue
        elif direction == "forward" and (xi==0 or xj==n-1):
            continue
        else:
            break

    while m>xi>=0 and 0<=xj<n:
        x[xi][xj]=1
        if direction=='back':
            xi-=1
            xj-=1
        elif direction == 'forward':
            xi-=1
            xj+=1
    return x