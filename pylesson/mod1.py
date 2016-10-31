import random
# help(random)
print(random.randint(1,10))
from random import choice
print(choice(['Ркуслан','Икса','Анкдрей']))
from random import *
print(randint(1,5))
# from a import write
# from b import write
# print(write('123'))

import a
a.write_me('Арксен')
from a import write_me
write_me('Икса')
import b as isa
isa.write_me('Рукслан')
print(isa.r_0())
from a import write_me
from b import write_me as write_me2
write_me('Икса')
write_me2('Икса')

# import sys
# # print(sys.argv)
# if len(sys.argv) < 3:
#     sys.exit()
# else:
#     print("{0} + {1} молодцы".format(sys.argv[1],sys.argv[2]))

# import base64
# left_align_png = 'loh.jpg'
# binary = open(left_align_png, "rb").read()
# ascii_text = ""
# for i, c in enumerate(base64.b64encode(binary)):
#     if i and i % 68 == 0:
#         ascii_text += "\\\n"
#     ascii_text += chr(c)
# print(ascii_text)

img = b"/9j/4AAQSkZJRgABAQEAeAB4AAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMF\
BwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYD\
AwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM\
DAwMDAz/wAARCACXANUDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQF\
BgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEI\
I0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNk\
ZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLD\
xMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEB\
AQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJB\
UQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZH\
SElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaan\
qKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oA\
DAMBAAIRAxEAPwD9/KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKK\
KACiiigAooooAKKKKACiiigAooooA8s/a+/a+8J/sT/CdPGHjBdVm0+a+j023g06BZri\
4ndXcKoZkUfJHIxLMBhfXAOh+zB+1D4S/a9+E9t4x8GXc1xpk0r200VxGI7iynQKWhlU\
EhXAZTwSCGUgkEV49/wWY+Fn/C0v+CefjjydM/tPUfDv2bXLPH3rTyJ0+0TDn+G1a5z/\
ALJavLf+Ddr/AJMp8Uf9jvd/+kGn14ssdXjmiwrtyON/O5+sUOEcpr+HtXiODksVSxCp\
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\
btZaH//Z"

import base64
binary = base64.b64decode(img)

open('loh2.jpg', "wb").write(binary)

import os