import requests
from bs4 import BeautifulSoup

def my_abs(x):

    if x > 0:
        return x
    else:
        return -x


if __name__ == "__main__":

    x = -9

    print(my_abs(x))

