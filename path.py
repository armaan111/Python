#/usr/bin/python3
import os

path="/root/test.txt"
print(os.path.basename(path))
print(os.path.dirname(path))

if os.path.exists(path):
    print("your file is there")
else:
    print("Its not there")

