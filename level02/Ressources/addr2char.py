import re
from termcolor import colored

data = input()
data = data.replace('0x', '')
liste = re.findall(r'([0-9a-f]{2,16})', data)
end = []
for s in liste:
    if len(s) < 3:
        end.append(s)
    else:
        he = re.findall('..', s)
        for i in reversed(he):
            end.append(i)

for i in end:
    c = chr(int(i, 16))
    if c == '\0':
        print(colored('|end|', 'red'), end='')
    elif c == '\n':
        print(colored('|LN|', 'green'), end='')
    elif re.match(r'[A-Za-z0-9]', c):
        print(colored(c, attrs=['bold']), end='')
    elif c.isascii():
        print(c, end='')
    else:
        print("-", end='')
