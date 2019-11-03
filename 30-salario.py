'''A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. 
Escreva uma função que receba o número dehoras trabalhadas em uma semana eo salário por hora, e retorne o salário do funcionário.'''

def hora_extra(hSemana,salHora):
    if hSemana <= 40:
        total = hSemana * salHora
    else:
        h_extra = (hSemana - 40) *(salHora+(salHora*0.5))
        total = (salHora*40)+h_extra
    return total

nome = input("Nome do funcionario: ")
hSemana = float(input("Horas trabalhadas na semana: "))
sHora = float(input("Salario hora: "))
salario = hora_extra(hSemana,sHora)
print("O sálario de %s é de R$%.2f"%(nome,salario))