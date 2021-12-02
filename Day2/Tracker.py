import sys

if __name__ == '__main__':
    File = sys.argv[1]
    with open(File) as f:
        lines = f.read().splitlines()
    
    Z = 0
    X = 0
    aim = 0

    for i in lines:
        i = i.split()
        if i[0] == "forward":
            X += int(i[1])
            Z += aim * int(i[1])
        if i[0] == "down":
            aim += int(i[1])
        if i[0] == "up":
            aim -= int(i[1])

    print("HPos:{} | VPos:{} | Prod:{}".format(Z, X, Z*X))