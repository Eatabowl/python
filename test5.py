#!/usr/bin/env python3

def my_abs(x):
    """TODO: Docstring for my_abs.

    :x: TODO
    :returns: TODO

    """
    if x>=0:
        return x
    else:
        return -x

if __name__ =="__main__":
    x =-8
    x = my_abs(x)
    print(x)
