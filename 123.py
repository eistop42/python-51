import re

s = """
There maybe misleading numbers in the 
text. One example is 82683. Look only for the next nothing and the next nothing is 63579
"""
r = re.findall(r'\d+', s)[-1]
print(r)