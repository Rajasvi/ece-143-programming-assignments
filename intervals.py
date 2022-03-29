class Interval(object):
    ''' This class handles Interval data structure and addtion operation for merging them.'''

    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b

    def __repr__(self):
        return f"Interval({self._a},{self._b})"
    def __eq__(self,other):
        return self._a == other._a and self._b == other._b
    def __lt__(self,other):
        return self._b < other._a 
    def __gt__(self,other):
        return self._a > other._b 
    def __ge__(self,other):
        return  self._b > other._a and self._a<other._b 
    def __le__(self,other):
        return self._a < other._a and self._b> other._a
    
    def __add__(self,other):
        assert isinstance(other, Interval)
                
        if self>other or other>self:
            if self>other:
                return [other,self]
            return [self,other]
        else:
            left = min(self._a,other._a)
            right = max(self._b,other._b)
            return Interval(left,right)