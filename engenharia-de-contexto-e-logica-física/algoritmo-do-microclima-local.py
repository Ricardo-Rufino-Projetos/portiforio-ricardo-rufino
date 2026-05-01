def classificar_iqa(iqa):
    match iqa:
        case _ if iqa <= 40:
            return "Boa"
        case _ if iqa <= 80:
            return "Moderada"
        case _ if iqa <= 120:
            return "Ruim"
        case _ if iqa <= 200:
            return "Muito Ruim"
        case _:
            return "Péssima"


def calcular_conforto(temp, umidade, iqa):
    penal_temp = abs(temp - 24) * 0.3

    penal_umidade = abs(umidade - 50) * 0.1

    penal_iqa = iqa * 0.05

    nota = 10 - (penal_temp + penal_umidade + penal_iqa)

    if nota < 0:
        nota = 0
    elif nota > 10:
        nota = 10

    return round(nota, 2)


def analisar_microclima():
    dados_locais = [
        ["Shopping Itaquera", 18, 90, 35],
        ["Estação Ferraz de Vasconcelos", 28, 16, 30],
        ["Radial Leste", 25, 70, 60]
    ]

    for local in dados_locais:
        nome = local[0]

        print(f"\n📍 Local: {nome}")

        for i in range(1, len(local)):
            if i == 1:
                print(f"Temperatura: {local[i]}°C")
            elif i == 2:
                print(f"Umidade: {local[i]}%")
            elif i == 3:
                print(f"IQA: {local[i]}")

        temp = local[1]
        umidade = local[2]
        iqa = local[3]

        qualidade = classificar_iqa(iqa)
        conforto = calcular_conforto(temp, umidade, iqa)

        print(f"Qualidade do Ar: {qualidade}")
        print(f"Nota de Conforto Urbano: {conforto}/10")


analisar_microclima()