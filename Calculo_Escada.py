vao=float(input("Digite o vão:"))
degrauIdeal=0.17
numDegraus=vao/degrauIdeal
espelho=vao/numDegraus
piso1=(2*(100*espelho))-63
piso2=(2*(100*espelho))-64
print(" Vão:{}\n Número de degraus:{}\n Espelho:{}\n Piso1:{}\n Piso2:{}".format(vao,numDegraus,espelho,piso1,piso2))
input()

