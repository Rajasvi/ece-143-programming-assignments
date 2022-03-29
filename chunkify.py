import os


def split_by_n(fname, n=3):
    """This function divides the file into equal-sized n chunks that no lines are truncated. 

    Args:
        fname (str): filepath for source txt file.
        n (int, optional): Number of splits to be created. Defaults to 3.
    """

    assert isinstance(fname, str), "Checks whether the file path is string or not."
    assert os.path.exists(fname), "File not found in the given path"
    assert isinstance(n, int), "Chunk size must be integer"
    assert n > 0, "Chunks can't be less than or equal to 0"

    chunkSize = os.path.getsize(fname) / n
    currChunkSize = 0
    newFileFlag = 1
    c = 0

    with open(fname, "r") as f:
        while c < n:
            l = f.readline()
            if len(l) == 0:
                break

            if currChunkSize + len(l) > chunkSize and c != n - 1:
                c += 1
                newFileFlag = 1
                currChunkSize = 0

            if newFileFlag:
                targetFile = open(fname + f"_{c:03d}.txt", "a")

            currChunkSize += len(l)
            targetFile.write(l)
