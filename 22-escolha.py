def animal():
    print("As perguntas devem ser respondidas com S ou N")
    p1 = input("É mamifero? ")
    if p1 == "S":
        p2 = input("É quadrupede? ")
        if p2 == "S":
            p3 = input("É carnivoro? ")
            if p3 == "S":
                animal = "leão"
            else:
                p4 = input("É herbivoro? ")
                if p4 == "S":
                    animal = "cavalo"
        else:
            p5 = input("É bipede? ")
            if p5 == "S":
                p6 = input("É onivoro? ")
                if p6 == "S":
                    animal = "homem"
                else:
                    p7 = input("É frutivoro? ")
                    if p7 == "S":
                        animal = "macaco"
            else:
                p8 = input("É voador? ")
                if p8 == "S":
                    animal = "morcego"
                else:
                    p9 = input("É aquatico? ")
                    if p9 == "S":
                        animal = "baleia"
    else:
        p10 = input("É uma ave? ")
        if p10 == "S":
            p11 = input("É voadora? ")
            if p11 == "N":
                p12 = input("É tropical? ")
                if p12 == "S":
                    animal="avestruz"
                else:
                    p13 = input("É polar? ")
                    if p13 == "S":
                        animal = "pinguim"
            else:
                p14 = input("É nadadora? ")
                if p14 == "S":
                    animal = "pato"
                else:
                    p15 = "É de rapina? "
                    if p15 == "S":
                        animal = "aguia"
        else:
            p16 = input("Repteis? ")
            if p16 == "S":
                p17 = input("Com casco? ")
                if p17 == "S":
                    animal = "tartaruga"
                else:
                    p18 = input("Carnivoro? ")
                    if p18 == "S":
                        animal = "crocodilo"
                    else:
                        p19 = input("Sem patas? ")
                        if p19 == "S":
                            animal = "cobra"
                        else:
                            animal = "nao encontrado"
    return print("O animal escolhido foi o/a {}".format(animal))

animal()