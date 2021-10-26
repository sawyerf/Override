# Level 08
<a href="/level09"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- Le fichier qu'on lit est reecrit dans le dossier backups
```
$> ~/level08 /home/users/level09/.pass
ERROR: Failed to open ./backups//home/users/level09/.pass
```
- On comprends que l'executable ne peut pas creer les dossier necessaire
- On n'a pas les droit dans le home pour creer les dossiers
- Donc il suffit de creer les dossiers dans /tmp/
```
$> cd /tmp/
$> mkdir -p ./backups//home/users/level09/
```
- Puis de executer l'executable
```
$> ~/level08 /home/users/level09/.pass
$> cat backups/home/users/level09/.pass 
fjAwpJNs2vvkFLRebEvAQ2hFZ4uQBWfHRsP62d8S
```
