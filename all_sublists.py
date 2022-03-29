def all_sublists(x):
    ''' This function generates all sublists i.e. 2**len(x) subset
    of list x. Ordering is ignored and func asserts against empty input array.
    '''
    assert isinstance(x,list)
    assert x!=[]
    unique_list = []
    for v in x:
        assert v!=[]
        if v not in unique_list:
            unique_list.append(v)
        else:
            assert v not in unique_list

    x_len=len(x)
    n = 2**x_len
    ans=[]
    for i in range(1,n):
        temp=i
        sublist=[]
        for j in range(x_len):
            if (temp & 1) == 1:
                sublist.append(x[j])
            temp=temp>>1
        ans.append(sublist)
    assert len(ans) == 2**len(x)-1
    return ans