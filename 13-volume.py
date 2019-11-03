def volume_esfera():
    import math
    raio = float(input("Digite o raio: "))
    volume = (4/3)*math.pi*(raio**3)
    return print("O volume é: %.2f"%(volume))

volume_esfera()