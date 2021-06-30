def multi(n, max):
    ### Renvoi la table de n jusqu'à i ###
    i = 1
    while i =< max:
        print(n, "x", i, "=", n * i)
        i += 1
n = 7
max = 15
print(multi(n, max))