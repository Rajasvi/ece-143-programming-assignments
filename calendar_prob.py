import calendar

def number_of_days(year,month):
    ''' This function is to find the number of days in a given month'''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert year>=0
    assert month>=1 and month<=12

    cal=calendar.Calendar()
    days = list(cal.itermonthdays(year=year,month=month))
    days = [x for x in days if x>0]
    return len(days)

def number_of_leap_years(year1,year2):
    ''' This function counts number of leap years in range [year1,year2]'''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1>=0 and year2>=0
   
    sumi=0
    for y in range(year1,year2+1):
        if calendar.isleap(y):
            sumi+=1     
    return sumi

def get_day_of_week(year, month, day): 
    ''' This function gives the name of day for a input date'''
    assert isinstance(year,int) and isinstance(month,int) and isinstance(day,int)
    assert year>=0 and (month<=12 and month>0) and (day>0 and day<32)
    
    return calendar.day_name[calendar.weekday(year,month,day)]
    