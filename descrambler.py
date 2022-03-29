import itertools as it
from collections import defaultdict, Counter


def descrambler(w, k):
    """This generator yields all outcomes which descrambles the word into k paritions with each partition representing a word from given common
    word dictionary."""
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    assert len(w) == sum(k)
    assert " " not in w

    word_map = defaultdict(set)
    with open("/tmp/google-10000-english-no-swears.txt", "r") as f:
        while True:
            l = f.readline()

            if not l:
                break
            temp = l.strip()
            if len(temp) not in k:
                continue
            word_map[len(temp)].add(temp)

    ans_set = set()

    def gen(tot_part, freq_c, k_part, words):
        if k_part >= tot_part:
            if " ".join(words) not in ans_set:
                ans_set.add(" ".join(words))
            return
        for word in word_map[k[k_part]]:
            source_counter = dict(Counter(word))
            target_counter = dict(freq_c.copy())
            f = 0
            for s_key, s_f in source_counter.items():
                if s_key in target_counter and target_counter[s_key] >= s_f:
                    target_counter[s_key] -= source_counter[s_key]
                else:
                    f = 1
                    break
            if f == 1:
                continue
            else:
                words.append(word)
                gen(tot_part, target_counter, k_part + 1, words)
                words.pop()

    gen(len(k), Counter(w), 0, [])

    for i in list(ans_set):
        yield i

