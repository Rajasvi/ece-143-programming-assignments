import numpy as np


def solvefrob(coefs, b):
    """This function solved Forbenius equation of format:
    a_1*x_1 + ....a_n*x_n = b.

    Args:
        coefs (list): List of a_i coefficients 
        b (int): Value of RHS in Forbenius equation

    Returns:
        list(tuple): All possible solution tuples for the equation.
    """

    assert isinstance(
        coefs, list
    ), "Check whether the coefficients list is there or not."
    assert isinstance(b, int), "Check whether the RHS is integer or not."
    assert all(
        co > 0 for co in coefs
    ), "Check all coeffcients are greater than zero or not."
    assert b > 0, "Check all coeffcients are greater than zero or not."

    limits = []  # Max feasable value acceptable for each coefficient.

    for c in coefs:
        assert isinstance(c, int), "Check all coefficients are integers or not."
        limits.append(b // c)

    for i, c in enumerate(coefs):
        temp = np.arange(limits[i] + 1)
        for j in range(i):
            temp = temp[:, np.newaxis]
        limits[i] = c * temp

    eq_sum = sum(limits) == b
    np_tuples = np.flip(np.transpose(np.nonzero(eq_sum)))
    answer = []
    for i in range(len(np_tuples)):
        answer.append(tuple(np_tuples[i]))

    return answer
