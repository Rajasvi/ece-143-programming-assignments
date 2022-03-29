def is_string_integer(s):
    '''This function checks whether the string is 
    a valid integer in base 10
    '''
    assert len(s)==1
    if ord(s)<58 and ord(s)>47:
        return True
    return False