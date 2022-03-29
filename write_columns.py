def write_columns(data, fname):
    '''This function writes the data from list in three columns with following values per column:
    data_value, data_value**2, (data_value+data_value**2)/3
    '''
    assert isinstance(data, list)
    assert isinstance(fname, str)
    with open(fname,'w') as f:
        for d in data:
            assert isinstance(d,float) or isinstance(d,int)   
            f.write(f'{d:.2f},{d**2:.2f},{(d+d**2)/3.0:.2f}')
            f.write("\n")