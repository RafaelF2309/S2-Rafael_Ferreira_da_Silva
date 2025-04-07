def calcular_imc():
    peso = input("Informe seu peso (kg): ")
    altura = input("Informe sua altura (m): ")
    
    if peso and altura:
        print("Dados recebidos.")
    else:
        print("Você precisa informar peso e altura.")

calcular_imc()
