import math
print(math.sqrt(8))
from math import sqrt
print(sqrt(4))
from math import *
print(sin(1))
from said_kharlik import do_eavl, obozvat
from said_holop import do_eavl as chert
do_eavl()
chert()
import random as r
print(r.random())

import paket.s1 as s1
print(s1.s)
from paket.s2 import celofan
celofan()

# help(math)
from random import randrange
print(randrange(1,6,2))

import datetime
td = datetime.date.today()
print(td)

import base64
# left_align_png = 'loh.png'
# binary = open(left_align_png, "rb").read()
# ascii_text = ""
# for i, c in enumerate(base64.b64encode(binary)):
#     if i and i % 68 == 0:
#         ascii_text += "\\\n"
#     ascii_text += chr(c)
# print(ascii_text)

img = b"""iVBORw0KGgoAAAANSUhEUgAAAGAAAABWCAIAAAC/2QTfAAAAAXNSR0IArs4c6QAAAARn\
QU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAUNSURBVHhe7ZVRjuQ2DET3\
IPnM/W+WM0yUVC2XTVFUSbK7Bxg/FAZuVpHyErb319dDybOgCc+CJjwLmvAsaMJkQf/8\
9TevfirVgtp2IP7+kQwXZNv54Tt6FjRBWhBLPxLpG/STd5QvCBs5XJBv78XQt+euV8y3\
p2Lu2zN8gk7+MaF9JKY/h3Ib0oKaaAiExlrseTv6bVz/BIXeWux5L+EeTLRfSRYU2iB6\
M5SuaaBRWJeA+f42Rid+eEEQjd+M6pdjBxVnXfwNUlp8xkSvc1m9B+Ws+RPEqoDeGJJN\
ND63IJY6pFeMxoylrhBuSuso3oRyVlxQ6DHRHrOab6QtodiE+h0oB0kLojdjOx+6RvU7\
mJ5y2RPUWAo3LN+3eAuicSnKEdJHGn8LfH4aNuqu2r0EZf41TxACYtiw/KjFB0aZE5T5\
13yDlsKG0uUzRWyDMLmJxivSK1YT8k00BKZd08AefixEo+OyV0xMepQun4FoHCPOnD9B\
TTTGrOaBz9ddloRYPUCf9sknqCE2+lidVAjTmmhkSE9QE70MPRlYalwKK4ij1FcMf3t8\
DKKhoXdZ0oveOvqQZEEN32+i9wrqdWaEdYm9Id9EY4XVCeo3qImJV5TMiI3e0ALR00Be\
771yQSzJ+F69PXRB9ARWu14W5JvR768LxFhgrwtYr4nGjNWWyRPkKwgEzC0yI7YbG77X\
RG/Mar4xfILCT1RSlEzPXpfHTzDRG7AUBuo3iHaHGEvZ6wrYEBONAXoSHH2DzB0FRvhG\
iMYW+iifqZPG8Any11bx1G7NSe8IZaCSCeRPEK77YsCs1K056e3x0yAar0wDPeorZhWj\
sKac9BbUY1EZuSMWFoSMp7BqrHGvfUQx01u9WzBcEEvjLVi9t6ac9NaMJvt6sGr+LCgd\
0Vc8tTvCdy01Tikmj+pT5k9QI62nRYXtRgU/3M/HdSgq5E8QS78ZWaP6CJ+HaFxHmN/U\
F5EUmS/I1wuLpRkbLav4I3oxJDP5BoG07ou+XrDRsk04q4nGIlxQmNWEOkittFizmt/G\
H2Sit8jyN8jctFiz0bJHOKiJxjr/LQj99SxzLeArVqxZCp9gB3nRWyR5xVAJpK4VQz3F\
h5X8IVcdJy0oddPiCB9W8ieEs7yYWCEuCD8D5vpMWkwJySYaNxAOCmJohZcF4QKVAALe\
tUqo94ixc/xBUCgitgQ/0vWINOCLvt6jJw9JD0qLOnFB6Yg00FdG6MlD/EH+rLQoIn2k\
Gz6ATF9JEWMnhCMgesc3ID1BjTTTV3p8pohtE+ZD9P6nsBSkbxDoY+FnjwXq2DZhPkTP\
Ubs1+09QX+mZBrbxk030OsRYyi+xOcSaQhExj3chGmf0M+1ihIWnyZ7NVwzJvuIprG1s\
mk22ypTVPPjzvxguasIB9tMrtVA8JMw00Z6x18UF6fgD7LoWGg/x0/y1iLV40StZW1B/\
QKikQu8J/bS9sX6OOOFoQU1p0QuN24RpEL11NuacLkgRmxcJQ0y0t9gY9Y4FNbFfpm/H\
30P8TIjGmP2PdKEQQ6OIb4RQhHuOnwzRGLC8oAaG2nRc2E+jrxTYhFQMXcTS8J0FXU64\
Yy8mrkaf/4EF+TuzGw2Chcwd+LPqg969oHBnvZi7HzuuPvStC8I91WL0Zvxx9aHfa0HM\
3Y9+7sdeMbtG/c3YbUzv4ZMf6frObgX3YGI14wML+g48C5rwLGiCuJ3Gs6DJjp4FlQv6\
+voXOS+jzudbkfIAAAAASUVORK5CYII="""

b = base64.b64decode(img)

open('loh2.png', "wb").write(b)

import sys
print(sys.argv)
if len(sys.argv) < 3:
    sys.exit()
else:
    print("{0[1]} + {0[2]} = <3".format(sys.argv))