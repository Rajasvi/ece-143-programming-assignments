import re, string
import os


def encrypt_message(message, fname):
    """Given `message`, which is a lowercase string without any punctuation, and `fname` which is the name of a text file source for the codebook, generate a sequence of 2-tuples that represents the `(line number, word number)` of each word in the message. The output is a list of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 

    Args:
        message ([str]): [given message to be encrypted]
        fname ([str]): [given filename for codebook]
    
    Returns:
        [list]: [encrypted message 2-tuple list]
    """

    assert isinstance(message, str), "Check whether message is string or not."
    assert isinstance(fname, str), "Checks whether the file path is string."
    assert os.path.exists(fname), "File not found in the given path."

    with open(fname, "r") as f:
        mapi = {}
        cnt = 1
        p = re.compile("[%s]" % re.escape(string.punctuation))

        while True:
            line = f.readline()
            if line == "":
                break
            line = p.sub("", line).lower()
            for i, w in enumerate(line.split(" ")):
                mapi[w] = (cnt, i + 1)

            cnt += 1
    encrypted = []
    for w in message.split(" "):
        assert w in mapi.keys(), "word in message is not in file.txt"
        encrypted.append(mapi[w])
    return encrypted


def decrypt_message(inlist, fname):
    """Given `inlist`, which is a list of 2-tuples`fname` which is the name of a text file source for the codebook, return the encrypted message.

    Args:
        inlist ([list]): [list of words to be decrypted]
        fname ([str]): [given filename for codebook]

    Returns:
        [str]: [decrypted message]
    """
    mapi = {}
    with open(fname, "r") as f:
        mapi = {}
        cnt = 1
        p = re.compile("[%s]" % re.escape(string.punctuation))
        p = re.compile(f"[{re.escape(string.punctuation)}]")
        while True:
            line = f.readline()
            if line == "":
                break
            line = p.sub("", line).lower()
            mapi[cnt] = line.split(" ")
            cnt += 1

    decrypted = []
    for line, wcount in inlist:
        assert line in mapi.keys(), "check whether valid line number is provided or not"
        assert wcount - 1 < len(
            mapi[line]
        ), "check whether valid word number is provided or not"
        decrypted.append(mapi[line][wcount - 1])
    return " ".join(decrypted)

