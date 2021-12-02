import numpy as np
import sys

if __name__ == '__main__':
    File = sys.argv[1]
    rows = np.loadtxt(File)
    print(np.sum(np.diff(rows)>0))
    rows = rows[0:-2] + rows[1:-1] + rows[2:]
    print(np.sum(np.diff(rows)>0))
