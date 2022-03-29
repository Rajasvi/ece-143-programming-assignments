def convert_hex_to_RGB(hex_list):
    ''' This function converts list of hexadecimal color codes to RGB-tuples.'''
    rgb_list=[]
    for hex in hex_list:
        assert isinstance(hex,str)
        assert len(hex)==7
        r=int(hex[1:3],16)
        g=int(hex[3:5],16)
        b=int(hex[5:],16)
        rgb_list.append( (r,g,b) )
    return rgb_list