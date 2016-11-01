import random
list1 = ['Тина','Гаджи','Хаджимурад','Азамат']
print(random.choice(list1))
import math
print(math.sqrt(4))
from random import choice
print(choice(list1))
from random import *
print(randint(1,100))

# from a import write_good
# from b import write_good
# write_good()
# help(math)

print(randrange(1,10,2))

# from a import *
# from b import *
# import a
# import b
from a import write_good, write_bad
from b import write_good as w_g

write_good()
w_g()
# write_bad(choice(list1))

# import sys
# # print(sys.argv)
# if len(sys.argv) < 3:
#     sys.exit()
# else:
#     print('{0[1]} + {0[2]} = <3'\
#         .format(sys.argv))

import base64
# left_align_png = 'loh.jpg'
# binary = open(left_align_png, "rb").read()
# ascii_text = ""
# for i, c in enumerate(base64.b64encode(binary)):
#     if i and i % 68 == 0:
#         ascii_text += "\\\n"
#     ascii_text += chr(c)
# print(ascii_text)

img = b"""/9j/4AAQSkZJRgABAQEAeAB4AAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMF\
BwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYD\
AwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM\
DAwMDAz/wAARCAArAEADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQF\
BgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEI\
I0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNk\
ZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLD\
xMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEB\
AQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJB\
UQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZH\
SElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaan\
qKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oA\
DAMBAAIRAxEAPwD84/8Agpj/AMkI0n/sPQ/+k9zWZ8DLOD4G/tYfFrR9Nm1az8EaF4fl\
8RXOnw/aLuGDy0t5VJRA5Oz7Q8SSSfcEvzyAF3rT/wCCmP8AyQjSf+w9D/6T3NUP28tI\
l+FWu+Ffin4cuv7M8TafeppzkWsLxXI2SyRu6lMSMArxsJd4eNo1wqx4b88yecJYWlha\
r92pzq3d3g16aXV/M/uLxRwuJocR5hxHgIJ1sD9Uqczs3GnKGJjNpNpS972cuW6vy7nn\
v7YH7Yfhr48/C/S9H0G18QW17Fqn2u6N7BFFEsSRFYwrJK5dmaRyQVUL5akFtx2fTHgv\
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"""

b = base64.b64decode(img)

open('loh2.jpg', "wb").write(b)
