f=open("graf.txt")
stare_initiala=f.readline()
stare_initiala=stare_initiala[0:len(stare_initiala)-1]
L=f.readlines()
sf=L[len(L)-1]
sf=sf.split()
tabela={}
cuvant=input("Cuvantul este:")

for i in range(0,len(L)-1):
    list=L[i].split()

    sursa=list[0]
    litera=list[1]
    destinatie=list[2]

    if sursa in tabela:
        tabela[sursa][litera]=destinatie
    else:
        tabela[sursa]={}
        tabela[sursa][litera]=destinatie


def accept(G,sf,initiala,cuv):
    stare=initiala
    drum=[stare]
    for c in cuv:
        try:
            stare=G[stare][c]
            drum.append(stare)
        except:
            return("Neacceptat")
    if stare in sf:
        print("Drumul:",*drum, sep='->')
        return("Acceptat")
    else:
        return("Neacceptat")

print(accept(tabela,sf,stare_initiala,cuvant))

f.close()