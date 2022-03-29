def write_chunks_of_five(words, fname):
    ''' This function writes a file with consecutibe non-overlapping sequences 
    of five words merged in one line.
    '''
    assert isinstance(words, list)
    assert isinstance(fname,str)
    n = len(words)
    with open(fname,'w') as f:
        for st in range(0,n,5):
            en = st+5 if st+5<=n else n
            for w in words[st:en]:
                assert isinstance(w,str)
            row = " ".join(words[st:en])
            print(row)
            f.write(row)
            f.write("\n")