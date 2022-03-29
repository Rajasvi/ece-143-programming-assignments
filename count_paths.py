from collections import defaultdict


def count_paths(m, n, blocks):
    """Starting at the upper left and only moving downwards and rightwards, this function finds the number of connected paths between the top-left square and the bottom right square by traversing non-blocked places.

    Args:
        m (int): number of horizontal rows.
        n (int): number of vertical columns.
        blocks (list):  list of tuples indicating the blocked entries in the grid.

    Returns:
        int: Number of possible unblocked paths from top-left ot bottom-right.
    """

    assert isinstance(m, int), "Check whether M is integer or not."
    assert m > 0, "Check whether m>0 or not."
    assert isinstance(n, int), "Check whether N is integer or not."
    assert n > 0, "Check whether n>0 or not."

    assert isinstance(blocks, list), "Check whether Blocks is list or not."

    grid = [[0 for _ in range(n)] for _ in range(m)]
    for b in blocks:
        assert all(x >= 0 for x in b), "Check all blocks coordinates are legit or not."

        if b[0] == 0 and b[1] == 0:  # Check if the starting point is blocked itself.
            return 0

        grid[b[0]][b[1]] = 1

    visited = defaultdict(int)

    def crawl(i, j, visited):
        """This function crawls through the grid in DFS fashion avoiding the blocks to check whether bottom-rightmost end can be reached or not. 

        Args:
            i (int): x-coordinate
            j (int): y-coordinate
            visited (dict): dictionary of visited coordinates.

        Returns:
            int: 1 if end can be reached otheewise 0.
        """

        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        path_sum = 0
        if i + 1 < m and visited[(i + 1, j)] == 0 and grid[i + 1][j] != 1:
            visited[(i + 1, j)] = 1
            path_sum += crawl(i + 1, j, visited)
            visited[(i + 1, j)] = 0

        if j + 1 < n and visited[(i, j + 1)] == 0 and grid[i][j + 1] != 1:
            visited[(i, j + 1)] = 1
            path_sum += crawl(i, j + 1, visited)
            visited[(i, j + 1)] = 0
        return path_sum

    return crawl(0, 0, visited)

