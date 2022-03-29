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

def map_bitstring(l):
    ''' This func takes a list of bitstrings (i.e., 0101) and maps each bitstring 
    to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s
    '''
    assert isinstance(l,list)
    strings = list(set(l))    
    ans = {}
    for s in strings:
        assert isinstance(s,str)
        intString = []
        for b in s:
            assert b=='1' or b=='0'
            intString.append(int(b))

        if sum(intString)>=len(intString)-sum(intString):
            ans[s]=1
        else:
            ans[s]=0
    return ans

def gather_values(x):
    '''This func generates n samples and tally the number of times an 
    existing key is repeated. Generate a new dictionary with 
    bitstrings as keys and with values as lists that contain 
    the corresponding mapped values from map_bitstring.
    '''
    assert isinstance(x,list)
    bit_map = map_bitstring(x)
    freq_map = {}
    for b in x:
        if b not in freq_map:
            freq_map[b]=[]
        freq_map[b].append(bit_map[b])
    return freq_map