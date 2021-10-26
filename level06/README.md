# Level 06
<a href="/level07"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- La premiere condition pour passer est que le premiere argument est une longueur de plus de 5
<pre>
gdb-peda$ disass auth
Dump of assembler code for function auth:
   ...
   0x080487b5 <+109>:   call   0x80485f0 <ptrace@plt>
   0x080487ba <+114>:   cmp    eax,0xffffffff
   ...
   0x08048863 <+283>:   mov    eax,DWORD PTR [ebp+0xc]
   0x08048866 <+286>:   cmp    eax,DWORD PTR [ebp-0x10]
   0x08048869 <+289>:   je     0x8048872 <auth+298>
   0x0804886b <+291>:   mov    eax,0x1
   0x08048870 <+296>:   jmp    0x8048877 <auth+303>
   0x08048872 <+298>:   mov    eax,0x0
   0x08048877 <+303>:   leave  
   0x08048878 <+304>:   ret    
End of assembler dump.
gdb-peda$ b \*0x080487ba
Breakpoint 1 at 0x80487ba
gdb-peda$ b \*0x08048866
Breakpoint 2 at 0x8048866
gdb-peda$ r < <(echo AAAAAA; echo 999)
Starting program: /home/alarm/42/override/level06/Ressources/level06 < <(echo AAAAAA; echo 999)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*               level06           \*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
-> Enter Login: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
\*\*\*\*\* NEW ACCOUNT DETECTED \*\*\*\*\*\*\*\*
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
[-------------------------------------code-------------------------------------]
   0x80487a6 <auth+94>: mov    DWORD PTR [esp+0x4],0x0
   0x80487ae <auth+102>:        mov    DWORD PTR [esp],0x0
   0x80487b5 <auth+109>:        call   0x80485f0 <ptrace@plt>
=> 0x80487ba <auth+114>:        cmp    eax,0xffffffff
   0x80487bd <auth+117>:        jne    0x80487ed <auth+165>
   0x80487bf <auth+119>:        mov    DWORD PTR [esp],0x8048a68
   0x80487c6 <auth+126>:        call   0x8048590 <puts@plt>
   0x80487cb <auth+131>:        mov    DWORD PTR [esp],0x8048a8c
[------------------------------------stack-------------------------------------]

Breakpoint 1, 0x080487ba in auth ()
gdb-peda$ set $eax=0x0
gdb-peda$ c
[-------------------------------------code-------------------------------------]
   0x804885e <auth+278>:        cmp    eax,DWORD PTR [ebp-0xc]
   0x8048861 <auth+281>:        jl     0x804880f <auth+199>
   0x8048863 <auth+283>:        mov    eax,DWORD PTR [ebp+0xc]
=> 0x8048866 <auth+286>:        cmp    eax,DWORD PTR [ebp-0x10]
   0x8048869 <auth+289>:        je     0x8048872 <auth+298>
   0x804886b <auth+291>:        mov    eax,0x1
   0x8048870 <auth+296>:        jmp    0x8048877 <auth+303>
   0x8048872 <auth+298>:        mov    eax,0x0

Breakpoint 2, 0x08048866 in auth ()
gdb-peda$ x $ebp-0x10
0xffffd528:     0x005f0c3a
gdb-peda$ x $eax
0x3e7:  Cannot access memory at address 0x3e7
</pre>
- 0x005f0c3a = 6 229 050
- Le deuxieme argument doit donc etre egale a  6 229 050
