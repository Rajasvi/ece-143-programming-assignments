
def compute_average_word_length(instring, unique=False):
    ''' This function evaluates the average length of words in input string.
    :unique: if True, duplicated words are counted once.
    '''
    words = instring.replace("\n"," ").split(" ")
    cnt_dict = {}
    for w in words:
        if w=="":
            continue
        assert len(w)>0
        if w not in cnt_dict:
            cnt_dict[w]=0
        cnt_dict[w]+=1
    sumi=0
    n=0
    print(cnt_dict)
    for w,c in cnt_dict.items():
        if unique:
            sumi+=len(w)
            n+=1
        else:
            sumi+=len(w)*c
            n+=c
    return float(sumi)/n