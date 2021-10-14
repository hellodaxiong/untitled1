import os
import sys

print(sys.platform)

path = './test1'
is_exits = os.path.exists(path)
if not is_exits:
    os.makedirs(path)
    print(path + ' created successfully.')
else:
    print(path + ' has already exists.')
