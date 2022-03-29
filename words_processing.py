from collections import Counter

def get_average_word_length(words):
    ''' This function evaluates the average length of words from input list of words.'''

    assert isinstance(words, list)
    assert len(words)!=0

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
    for w,c in cnt_dict.items():
        sumi+=len(w)*c
        n+=c
    return float(sumi)/n

def get_longest_word(words):
    ''' This function returns the longst word from given words list.'''

    assert isinstance(words,list)
    assert len(words)!=0

    maxWordLen = 0
    longestWord = ""
    for w in words:
        assert isinstance(w,str)
        if len(w) >= maxWordLen:
            maxWordLen = len(w)
            longestWord = w
    
    assert longestWord!=""
    return  longestWord 
 
def get_longest_words_startswith(words,start):
    ''' This function returns the longest word that starts with given single character "start"
    from the given words list.
    '''

    assert isinstance(words,list)
    assert len(words)!=0
    assert(isinstance(start,str))
    
    maxWordLen = 0
    longestWord = ""

    for w in words:
        assert isinstance(w,str)
        if w.startswith(start) and len(w)>=maxWordLen:
            maxWordLen=len(w)
            longestWord = w
            
    assert longestWord!=""
    return  longestWord 
 
def get_most_common_start(words):
    ''' This function return the most commmon starting letter in word list.'''

    assert isinstance(words,list)
    assert len(words)!=0

    firstCharList = []
    for w in words:
        assert isinstance(w,str)
        assert len(w) != 0
        firstCharList.append(w[0])
    return Counter(firstCharList).most_common(1)[0][0]

def get_most_common_end(words):
    ''' This function return the most commmon ending letter in word list.'''

    assert isinstance(words,list)
    assert len(words)!=0

    lastCharList = []
    for w in words:
        assert isinstance(w,str)
        assert len(w) != 0
        lastCharList.append(w[-1])
    return Counter(lastCharList).most_common(1)[0][0]