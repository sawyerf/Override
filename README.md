export FILE=level02; mkdir $FILE; cd $FILE; touch source; touch flag; mkdir Ressources; cd Ressources; scp -P 4242 $FILE@192.168.1.50:/home/users/$FILE/$FILE .
