#!/usr/local/bin/python3.6
from sys import argv
def unix2dos(fname,end="\r\n"):
    new_fname=fname+".txt"
    with open(fname,"r") as src_file:
        with open(new_fname,"w") as dst_file:
            for line in src_file:
                dst_file.write(line.rstrip()+ end)

if __name__ == "__main__":
    unix2dos(argv[1])
