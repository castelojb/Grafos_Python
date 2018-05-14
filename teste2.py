# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys

    
if __name__ == "__main__":
    programa=[]
    siga=True
    
    while siga:
        linha=input()
        if linha != "":
            programa.append(linha)
        else:
            siga=False
        
    
    
    cont=0
    Grafo=[]
    for linha in programa:
        linha=linha.split()
        
       
        cont=cont+1
        
        if cont==3:
            
            vertices= int(linha[0].replace("n=",""))
            cont=cont+1
            for i in range(0,vertices,1):
                Grafo.append([i])
        
        if cont>5:
            
            pos=int(linha[0])-1
            elo=[]
            for g in range(1,len(linha),1):
                elo.append(int(linha[g])-1)
            
            Grafo[pos]=elo+Grafo[pos]
            
            for r in elo:
                #print("Grafo para a volta ",Grafo[r-1])
                Grafo[r].append(pos)
                
    for K in range(0,vertices,1):
        Grafo[K]=sorted(Grafo[K])
    
    
    
    for x in range(0,vertices,1):
        if Grafo[x]!=[]:
            y=0
            while y< len(Grafo[x]):
                
                if Grafo[Grafo[x][y]]!= [] and Grafo[Grafo[x][y]] != Grafo[x]:
                   
                    a=Grafo[x]
                    b=Grafo[Grafo[x][y]]
                    c=[]
                    for a1 in a:
                        c.append(a1)
                    for a2 in b:
                        if a2 not in c:
                            c.append(a2)
                    
                    Grafo[x]=c
                    
                    Grafo[Grafo[x][y]]=[]
                    
                    y=0
                else:
                    y=y+1
        
    
    for K in range(0,vertices,1):
        Grafo[K]=sorted(Grafo[K])
        
        
    
    
    grafo2=[]
    for K in range(0,vertices,1):
        grafo2.append([])
        if Grafo[K] not in grafo2:
            grafo2[K]=Grafo[K]
    
    for resp in grafo2:
        linha=""
        
        if resp != []:
            total=len(resp)
            aux=0
            for elemento in resp:
                aux=aux+1
                if aux!=total:
                    linha=linha+str(elemento+1)+ " "
                else:
                    linha=linha+str(elemento+1)
            
            print(linha,end="")

    



