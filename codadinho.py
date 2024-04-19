import os
import sys
import time
import shutil
import random

print ("originado no hh,um oferecimento COMICY")

time.sleep(2)
os.system("cls")
print ("2 seconds are up already")
time.sleep(0.5)
os.system("cls")

nome = input("Digite o nome da pessoinha: ")

vetorlaudos1 = [line.rstrip() for line in open('primeiro.txt')]
vetorlaudos2 = [line.rstrip() for line in open ('segundo.txt')]

xingada1 = random.choice(vetorlaudos1)
xingada2 = random.choice(vetorlaudos2)

print (nome + ' eh ' + xingada1  + ' ' + xingada2 )

input()
