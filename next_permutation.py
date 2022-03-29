def next_permutation(t):
    """Given a permutation of any length, generate the next permutation in lexicographic order.

    Args:
        t (tuple): input tuple

    Returns:
        tuple: next permutation 
    """
    assert isinstance(t, tuple), "Check whether the input is tuple or not."
    assert all(isinstance(x, int) for x in t) or all(
        isinstance(x, str) for x in t
    ), "Check all the inputs are of same type"

    assert len(t) == len(set(t)), "all unique elements or not"

    t = list(t)
    n = len(t)
    pos = n - 1

    # find position for next character till which tuples are in descending order
    while pos > 0 and t[pos - 1] > t[pos]:
        pos -= 1

    t[pos:] = reversed(t[pos:])

    # find the lead next position for generating lowest lexigraphic order.
    if pos > 0:
        next_pos = pos
        while t[pos - 1] > t[next_pos]:
            next_pos += 1

        t[pos - 1], t[next_pos] = t[next_pos], t[pos - 1]

    return tuple(t)

