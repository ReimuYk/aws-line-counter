import re
import sys
import os

# usage: python3 lambda_counter.py ./dir

def get_base_dir() -> str:
    return sys.argv[1]

def lambda_filter(path) -> bool:
    with open(path, "r", errors="ignore") as f:
        content = f.read()
        if "def lambda_handler" in content or "exports.handler" in content:
            return True
    return False

def statistics(path):
    print(path)
    if ".py" in path:
        # find "def lambda_handler" and count lines
        with open(path, "r", errors="ignore") as f:
            content = f.readlines()
            flag = False
            line_count = 0
            for line in content:
                if "def lambda_handler" in line:
                    flag = True
                if flag and line.replace("\t", "").replace(" ", "").replace("\n", "").replace("\r", "") != "":
                    line_count += 1
                    print(line_count, end="\t")
                    print(line.replace("\n", "").replace("\r", ""))
                # TODO: close flag
            print(line_count)
    # TODO: js files
    print()


for root, dirs, files in os.walk(get_base_dir(), topdown=False):
    for name in files:
        full_path = os.path.join(root, name)
        if lambda_filter(full_path):
            statistics(full_path)

