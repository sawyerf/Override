# Level 03
<a href="/level04"><img align='right' width=20x height=auto src="https://cdn.onlinewebfonts.com/svg/img_68680.png"></img></a>

- Dans le code on voit qu'il y a un switch
- Ce Switch compare 322424845 moins la variable d'entree a une liste de chiffre
- Il suffit de teste touts les chiffres et cela fonctionne
```
$> for number in {1..21}
do
echo -n level $number :
python -c "print(322424845 - $number)" | ./level03 | grep Invalid
done
level 1 :Invalid Password
level 2 :Invalid Password
level 3 :Invalid Password
level 4 :Invalid Password
level 5 :Invalid Password
level 6 :Invalid Password
level 7 :Invalid Password
level 8 :Invalid Password
level 9 :Invalid Password
level 10 :Invalid Password
level 11 :Invalid Password
level 12 :Invalid Password
level 13 :Invalid Password
level 14 :Invalid Password
level 15 :Invalid Password
level 16 :Invalid Password
level 17 :Invalid Password
level 18 :
level 19 :Invalid Password
level 20 :Invalid Password
level 21 :Invalid Password
```
