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