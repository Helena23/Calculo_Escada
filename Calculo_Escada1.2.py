
x=0
y=1
while(x<y):
    x=x+1
    y=y+1
    vao=float(input("Digite o vão:"))
    degrauIdeal=0.17
    numDegraus=vao/degrauIdeal
    espelho=vao/numDegraus
    conversorParaCm=100
    piso1=(2*(conversorParaCm*espelho))-63
    piso2=(2*(conversorParaCm*espelho))-64
    print(" Vão:{}\n Número de degraus:{}\n Espelho:{}\n Piso1:{}\n Piso2:{}".format(vao,numDegraus,espelho,piso1,piso2))
    flag=str(input("Digite C para continuar ou S para parar:"))
    if(flag == "S" or flag == "s"):
        x=x+1
        print("Obrigado por utilizar este programa!")
    if(flag == "C" or flag == "c"):
        x=x
        print("""
             _
            |
           _
          |
         _
        |
       _
      |""")
    
    else:
        pass
input()
        

