loop=int(input("Quantas vezes você deseja utilizar este programa?"))
x=0
while(x<loop):
    x=x+1
    vao=float(input("Digite o vão:"))
    degrauIdeal=0.17
    numDegraus=vao/degrauIdeal
    espelho=vao/numDegraus
    conversorParaCm=100
    piso1=(2*(conversorParaCm*espelho))-63
    piso2=(2*(conversorParaCm*espelho))-64
    print(" Vão:{}\n Número de degraus:{}\n Espelho:{}\n Piso1:{}\n Piso2:{}".format(vao,numDegraus,espelho,piso1,piso2))
    

