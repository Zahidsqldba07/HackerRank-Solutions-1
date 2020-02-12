import re

def fun(s):
    return re.match(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.{1}[a-zA-Z0-9]{1,3}$", s)

