Salir = False
while(Salir==False):
    print("1. Ejemplo1 \n2. Ejemplo2 \n3. Ejemplo3 \n4. Salir")
    Num = int(input())
    if(Num==1):
        L1 = ["a","b","2","3"]
        L2 = ["c","d","3","4"]
        L3 = []
        L4 = []
        S1 = set(L1)
        S2 = set(L2)
        L3 = (list(S1&S2))
        L4 = (list(S1^S2))
        L4.sort()
        print(f"{L3} {L4}")
    elif(Num==2):
        L1 = ["a","b","2","3"]
        L2 = ["c","d","4"]
        L3 = []
        L4 = []
        S1 = set(L1)
        S2 = set(L2)
        L3 = (list(S1&S2))
        L4 = (list(S1^S2))
        L4.sort()
        print(f"{L3} {L4}")
    elif(Num==3):
        L1 = ["a","b","2","2","3"]
        L2 = ["c","d","2","a","4"]
        L3 = []
        L4 = []
        S1 = set(L1)
        S2 = set(L2)
        L3 = (list(S1&S2))
        L4 = (list(S1^S2))
        L4.sort()
        print(f"{L3} {L4}")
    elif(Num==4):
        Salir = True
    