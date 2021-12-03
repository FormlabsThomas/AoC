import sys
import numpy as np

if __name__ == '__main__':
    File = sys.argv[1]
    with open(File) as f:
        lines = f.read().splitlines()
    out = []
    for i in lines:
        i = list(map(int, list(i)))
        out.append(i)

    out = np.array(out)
    gamma = np.sum(out, 0) > np.shape(out)[0]/2
    epsilon = 1-gamma
    Mask = np.flip(2**np.arange(0, np.shape(out)[1], 1))
    print("{} --> {}".format(1*gamma, np.sum(gamma * Mask)))
    print("{} --> {}".format(1*epsilon, np.sum(epsilon * Mask)))

    print(np.sum(gamma * Mask) * np.sum(epsilon * Mask))
