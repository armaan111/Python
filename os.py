#!usr/bin/python3
import os
cmd="date"
rt=os.system(cmd)
if rt==0:
    print("Your cmd was successfully executed")
else:
    print("command was not successfullly executed")
