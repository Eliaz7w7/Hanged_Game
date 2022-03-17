import os
import random


def run():
    # os.system("clear")
    print("Adivina la palabra")
    with open("./DATA/data.txt", "r", encoding="utf-8") as f:
        a=[a.strip() for a in f]
        abc=dict(enumerate(a,1)) 
    print(abc)

if __name__=="__main__":
    run()