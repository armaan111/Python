#!/usr/bin/python
import os
path="/home/ec2-user/"

if os.path.isfile(path):
    print(f"{path} is a file")
else:
    print(f"{path} is a not file")

