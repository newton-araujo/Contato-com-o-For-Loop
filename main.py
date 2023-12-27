#Pegamos o método sleep dentro da biblioteca time
from time import sleep

#Iniciando o for loop no range 1 até 11.
for contador in range(1,11):
    sleep(1) #Chamamos o método sleep com um delay de 1 segundo
    print(contador,end=' ')