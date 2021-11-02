# Level 03
<a href="/level04"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- Dans le code on voit qu'il y a un switch
- Ce Switch compare 322424845 moins la variable d'entree a une liste de nombre
- Il suffit de teste tout les nombre possible
```
$> for number in {1..21}
do
echo -n nb $number :
python -c "print(322424845 - $number)" | ./level03 | grep Invalid
done
nb 1 :Invalid Password
nb 2 :Invalid Password
nb 3 :Invalid Password
nb 4 :Invalid Password
nb 5 :Invalid Password
nb 6 :Invalid Password
nb 7 :Invalid Password
nb 8 :Invalid Password
nb 9 :Invalid Password
nb 10 :Invalid Password
nb 11 :Invalid Password
nb 12 :Invalid Password
nb 13 :Invalid Password
nb 14 :Invalid Password
nb 15 :Invalid Password
nb 16 :Invalid Password
nb 17 :Invalid Password
nb 18 :
nb 19 :Invalid Password
nb 20 :Invalid Password
nb 21 :Invalid Password
```
- On voit que le seul numero a ne pas avoir "Invalid Password" est le 18
- Donc il suffit de lancer la commande suivante
```
(python -c "print(322424845 - 18)" ; sleep 0.1; echo "cat /home/users/level04/.pass") | ./level03
```
