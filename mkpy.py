#!/usr/bin/env python3

import os, sys

def createFile(fname):
    with open(fname + ".py", "w") as pyFile:
        pyFile.write("#! /usr/bin/env python3\n") 
    os.system(f"chmod +x {fname}.py")

try:
    fname = str(sys.argv[1])
except IndexError:
    print("Usage: ./mkpy.py <name of script>")
else:
    if os.path.exists(fname + ".py"):
        ans = input(f"{fname}.py exists, overwrite? [y/n]: ")

        if ans == "y":
            os.remove(f"{fname}.py")
            createFile(fname)
        else:
            print("Exiting...")
            sys.exit(1)
    else:
        createFile(fname)
