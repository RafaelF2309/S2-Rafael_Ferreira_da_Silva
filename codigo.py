def calcular_imc():
    peso = input("Informe seu peso (kg): ")
    altura = input("Informe sua altura (m): ")
    
    if peso and altura:
        pezo = float (peso)
        altura = float (altura)
        imc = peso / altura * altura
        print ("Seu IMC é:", imc)
        
        if inc < 18.5:
            print("Abaixo do peso.")
        elif inc < 25:
            print("Peso ideal.")
        else
            print("Acima do peso.")
    else
        print("Você precisa informar peso e altura.")

calcular_imc()