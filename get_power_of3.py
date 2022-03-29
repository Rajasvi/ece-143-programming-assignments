import itertools as it


def get_power_of3(x):
    """ This function constructs number x using any possible 
    non-repeating combination of [1,3,9,27] i.e. by both adding/subtracting operations
    """
    assert isinstance(x, int)
    assert x <= 40 and x >= 1
    for v in it.product([1, -1, 0], repeat=4):
        s = sum([a * b for a, b in zip([1, 3, 9, 27], v)])
        if s == x:
            return list(v)
