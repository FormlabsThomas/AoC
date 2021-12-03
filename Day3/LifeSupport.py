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


    Out1 = np.array(out)
    Out2 = np.array(out)
    for i in range(np.shape(out)[1]):
        Bit = np.sum(Out1[:,i]) >= np.shape(Out1)[0]/2
        Out1 = Out1[np.argwhere(Out1[:,i] == Bit).flatten(), :]
        if np.shape(Out1)[0] == 1:
            break

    for i in range(np.shape(out)[1]):
        Bit = (np.sum((Out2[:,i])) >= np.shape(Out2)[0]/2)
        Out2 = Out2[np.argwhere(Out2[:,i] == (1-Bit)).flatten(), :]
        if np.shape(Out2)[0] == 1:
            break

    Mask = np.flip(2**np.arange(0, np.shape(out)[1], 1))
    print("{} --> {}".format(1*Out1.flatten(), np.sum(Out1 * Mask)))
    print("{} --> {}".format(1*Out2.flatten(), np.sum(Out2 * Mask)))

    print(np.sum(Out1 * Mask) * np.sum(Out2 * Mask))
