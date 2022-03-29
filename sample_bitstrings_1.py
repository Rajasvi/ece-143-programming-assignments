import itertools as it
import random

def get_sample(nbits=3, prob=None, n=4):
    ''' This func returns list of n samples from a finite PMF defined by dict prob
    with keys defined by specific num of bits.
    '''
    assert isinstance(prob,dict) and isinstance(nbits,int) and isinstance(n,int)
    assert nbits>0
    assert len(prob.keys())==pow(2,nbits)
    assert sum(list(prob.values()))==1

    keys=list(prob.keys())
    w = [prob[x] for x in keys]
    return random.choices(keys,w,k=n)