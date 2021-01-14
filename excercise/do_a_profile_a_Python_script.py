 # How to do a profile a Python script

import cProfile

def sum():
    print(1,3)

cProfile.run('sum()')