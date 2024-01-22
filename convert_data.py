import numpy as np
import sys, os

def convert_data(dir_name):
    adj = np.loadtxt(
        os.path.join(dir_name, "D.txt"),
        dtype=int
    )
    np.savetxt(
        os.path.join(dir_name, "directed_adjacency_matrix.csv"),
        adj,
        delimiter=",",
        fmt="%d"
    )
    adj = np.loadtxt(
        os.path.join(dir_name, "B.txt"),
        dtype=int
    )
    np.savetxt(
        os.path.join(dir_name, "bidirected_adjacency_matrix.csv"),
        adj,
        delimiter=",",
        fmt="%d"
    )
    x = np.load(
        os.path.join(dir_name, "X.npy")
    )

    np.savetxt(
        os.path.join(dir_name, "train.csv"),
        x,
        delimiter=",",
    )
    np.savetxt(
        os.path.join(dir_name, "test.csv"),
        x,
        delimiter=",",
    )
    np.savetxt(
        os.path.join(dir_name, "val.csv"),
        x,
        delimiter=",",
    )

if __name__ == "__main__":
    convert_data("data/test-n-admg")
    # for i in range(10):
    #     convert_data(f"data/10_{i}")