import types

def tracker(p,limit=1):
    ''' This function is to track the odd numbered seconds from 
    producer's output upto a given limit.
    |p|: producer 
    |limit|: tracking limit for odd numbered seconds 
    '''
    assert limit > 0
    assert isinstance(p,types.GeneratorType)
    sec=0
    sumi=0
    while sumi<limit:
        delta=next(p)
        sec=int(delta.total_seconds())
        if sec%2!=0:
            sumi+=1
        limitUpdate = (yield sumi)
        if limitUpdate!=None:
            assert limitUpdate>=limit
            limit = limitUpdate