import os
import random

# ENUMERAMOS LA PALABRA Y LO CONVERTIMOS A DICCIONARIOS
# DEVOLVEMOS LA VARIABLE ABC
def dic_pal():
    with open("./DATA/data.txt", "r", encoding="utf-8") as f:
        a=[a.strip() for a in f]
        abc=dict(enumerate(a,1)) 
    return (abc)

# ESCOJEMOS UN NUMERO AL AZAR 
# EN BASE AL NUMERO ESCOJEMOS la PALABRA DEL DICCIONARIO ANTERIOR
def azar():
    i=random.randint(1,len(dic_pal()))
    rm=dic_pal()[i]
    return rm

if __name__=="__main__":
    azar()