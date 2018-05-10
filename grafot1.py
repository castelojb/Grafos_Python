# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys


if __name__ == "__main__":
    Grafo=[]
    linha=[]
    vertices= int (input("Qual o tamanho do Grafo?: "))
    i=0
    print("para parar a ligacao do vertice, digite -999")
    while i < vertices:
        elo=int(input("diga a ligacao do vertice %s:" %i))
        if elo==-999:
            linha=sorted(linha)
            Grafo.append(linha)
            i=i+1
            linha=[]
        else:
            if elo not in linha:
                linha.append(elo)
    x0=0
    print(Grafo)
    for x0 in range(0,vertices,1):
        if Grafo[x0]!=[]:
            elemento=0
            while elemento < len(Grafo[x0]):
                print("Este eh o x0 ",Grafo[x0])
                print("Este eh o elemento avaliado: ",elemento)
                if Grafo[Grafo[x0][elemento]] != []:
                    a=Grafo[x0]
                    b=Grafo[Grafo[x0][elemento]]
                    c=[]
                    for k in a:
                        c.append(k)

                    for p in b:
                        if p not in c:
                            c.append(p)
                    c=sorted(c)
                    print("Entrada c ",c)
                    Grafo[x0]=c
                    Grafo[[x0][elemento]]=[]
                    print("grafo atl ", Grafo)
                    elemento=0
                else:
                    elemento=elemento+1
        print(Grafo)
    print(Grafo)
                
            
   # if 4 in Grafo[0]:
    #    print("OK")
     #   for K in range (0,len(Grafo[0]),1):
      #      if Grafo[0][K]==4:
       #         Grafo[0][K]=0
    #if 4 in Grafo[0]:
     #   print("n ok")
    
    
    
    
            
    
    