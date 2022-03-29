import random
from collections import Counter, defaultdict


def multinomial_sample(n, p, k=1):
    """Return samples from a multinomial distribution.

    Args:
        n (int): number of trials.
        p (list): list of probabilities.
        k (int, optional): number of desired samples. Defaults to 1.

    Returns:
        list: Returns list of sample counts from the multinomial distribution.
    """

    assert isinstance(n, int), "check whehter n is not integer"
    assert isinstance(p, list), "check whether probability is not a list"
    assert isinstance(k, int), "check whether k is integer or not"
    assert sum(p) == 1, "check whether sum of probability is 1.0 or not"
    assert k > 0, "check that number of samples requested are >1"

    samples = []
    for _ in range(k):
        sample = random.choices(range(len(p)), p, k=n)
        sampleCount = [0] * len(p)

        for key, value in Counter(sample).items():
            sampleCount[key] = value

        samples.append(sampleCount)

    return samples
