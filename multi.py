from random import randint as rd
n = rd(1,50000)
max = rd(5,50)

def multi(n, max):
    ### Renvoi la table de n jusqu'à i au hasard ###
    i = 1
    while i <= max:
        print(n, "x", i, "=", n * i)
        i += 1

print("Table de", n,"jusqu'à", max, ":")
multi(n, max)
