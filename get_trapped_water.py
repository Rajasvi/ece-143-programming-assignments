def get_trapped_water(seq):
    """Computes how many units of water remain trapped between the walls in the map.

    Args:
        seq (list): input list of elevations. 

    Returns:
        int: volume of water trapped.
    """
    assert isinstance(seq, list), "Check whether wall map is list or not."

    n = len(seq)
    rmax = [0]
    curr_max = seq[n - 1]

    for i in range(n - 2, -1, -1):
        assert isinstance(
            seq[i], int
        ), "Check whether all wall elevations are int or not."
        curr_max = max(curr_max, seq[i + 1])
        rmax.append(curr_max)

    rmax.reverse()

    lmax = seq[0]
    vol_water = 0
    for i in range(1, n):
        if lmax > seq[i] and rmax[i] > seq[i]:
            vol_water += min(lmax, rmax[i]) - seq[i]
        lmax = max(lmax, seq[i])

    return vol_water
