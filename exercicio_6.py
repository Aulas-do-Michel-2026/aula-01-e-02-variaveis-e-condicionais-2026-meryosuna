país= input("Qual país você vai viajar?:")
if país== "Estados unidos":
    reais=float(input("Quantos reais você quer converter?:"))
    dollar= reais/5
    print(f"{dollar:.2f} USD")                
elif país== "Argentina":
    reais=float(input("Quantos reais você quer converter?:"))
    pesos= reais*180
    print(f"{pesos:.2f} ARS")
elif país== "Japão":
    reais=float(input("Quantos reais você quer converter?:"))
    ienes= reais*30
    print(f"{ienes:.2f} JPY")
else :
    print("Não temos essa moeda em caixa.")   
