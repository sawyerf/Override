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
| level05 |                 |  |
| level06 |                 |  |
| level07 |                 |  |
| level08 |                 |  |
| level09 |                 |  |

## Command

```
export FILE=level02; mkdir $FILE; cd $FILE; touch source flag README.md; mkdir Ressources; cd Ressources; scp -P 4242 $FILE@192.168.1.50:/home/users/$FILE/$FILE .
```

```
(python -c "import struct; print('A' * 100 + struct.pack('<I', 0xffffffff))")
```
