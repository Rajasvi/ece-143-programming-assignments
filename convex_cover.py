import numpy as np
from collections import defaultdict


def find_convex_cover(pvertices, clist):
    """ For convex olygon with vertices as "pvertices" and circles inside it with cetners as "clist", this function calculates the radius such that sum of aras of circles is minimized and that vertex is contained in atleast one of the circles.

    Args:
        pvertices (np.array): List of vertex co-ordinates of polygon.
        clist (np.array): Co-ordinates of circle centers.

    Returns:
        list: List of radii for each circle center.
    """

    # Vertices Corrdinates
    x_v = pvertices[:, 0]
    y_v = pvertices[:, 1]

    # Center Corrdinates
    clist = np.array(clist)
    x_c = clist[:, 0]
    y_c = clist[:, 1]

    # Calculate distance of each circle center from every vertex.
    dist = np.sqrt(
        abs(x_v.reshape(-1, 1)[:, None] - x_c.reshape(-1, 1)) ** 2
        + abs(y_v.reshape(-1, 1)[:, None] - y_c.reshape(-1, 1)) ** 2
    )

    # Extract circle centers with distance which are closest to each vertex
    min_v = [
        (x, y)
        for x, y in zip(
            np.sort(dist, axis=1)[:, 0][:, 0], np.argsort(dist, axis=1)[:, 0][:, 0]
        )
    ]

    # For common closest centers, select the radius among all common radius which has max distance.
    mapi = defaultdict(int)
    for d, v in min_v:
        mapi[v] = max(mapi[v], d)

    # Final list with radius for each center
    ans = [mapi[i] for i in range(len(clist))]

    return ans

