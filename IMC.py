def cadastro():
    nome = input("Nome: ").title()
    idade = input("Idade: ")
    while True:  # Continuaremos tentantoa até o usuário inserir corretamente o valor.
        try:  # Esquema try, except para lidar com  o erro.
            # Caso o usuário use vírgula, dará erro na conversão para float. Usamos o replace para garantir o uso do '.'.
            peso = float(input("Peso (ex: 65.2): ").replace(",", "."))
        except:
            print("Houve um erro ao interpretar o seu peso. Tente novamente.")
            # Fará com que o loop volte do início, ou seja, vai solicitar denovo o peso do usuário.
            continue
        # Se não houver erro, o loop é quebrado e o código continua na execução normal.
        break
    while True:
        try:
            altura = float(input("Altura (ex: 1.70): ").replace(",", "."))
        except:
            print("Houve um erro ao interpretar a sua altura. Tente novamente.")
            continue
        break
    imc = round(peso / (altura ** 2), 1)
    return [nome, idade, peso, altura, imc]


def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc > 18.5 and imc < 24.9:
        return "Normal"
    elif imc > 25.0 and imc < 29.9:
        return "Sobrepeso"
    elif imc > 30.0 and imc < 39.9:
        return "Obesidade"
    else:
        return "Obesidade grave"


print("""
---------------------------------------------
*************** CALCULO DE IMC **************
---------------------------------------------
""")

formulario = cadastro()

print("\n\n***RESULTADO***\n\n")
print(f'NOME: {formulario[0]}')
print(f'IDADE: {formulario[1]} anos')
print(f'PESO: {formulario[2]}kg')
print(f'ALTURA: {formulario[3]}m')
print(f'SEU IMC ATUAL: {formulario[4]}')
print(f'CLASSIFICAÇÃO DO SEU IMC: {classificar_imc(formulario[4])}')
print("\n\nObrigado por fazer o teste!")
