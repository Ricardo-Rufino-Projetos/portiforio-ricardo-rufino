def simulador_evacuacao():
    locais = ["Quarto", "Sala", "Corredor", "Quintal", "Saida"]
    estados = ["livre", "chave", "porta_trancada", "corredor_livre", "livre"]

    posicao = 0
    energia = 10

    inventario = {
        "chave": False
    }

    print("Simulação iniciada!\n")

    while energia > 0:
        local_atual = locais[posicao]
        estado_atual = estados[posicao]

        print(f" Local: {local_atual}")
        print(f" Estado: {estado_atual}")

        if local_atual == "Saida":
            print(" Você escapou com sucesso!")
            break

        # Lógica principal
        if estado_atual == "livre":
            print(" Caminho livre")
            posicao += 1

        elif estado_atual == "corredor_livre":
            print("Corredor livre, avanço rápido")
            posicao += 1

        elif estado_atual == "chave":
            print(" Chave encontrada!")
            inventario["chave"] = True
            posicao += 1

        elif estado_atual == "porta_trancada":
            print(" Porta trancada!")

            if inventario["chave"]:
                print(" Porta aberta com a chave")
                posicao += 1
            else:
                print(" Sem chave, voltando...")
                posicao -= 1

        # Controle de limites
        if posicao < 0:
            posicao = 0
        elif posicao >= len(locais):
            posicao = len(locais) - 1

        energia -= 1
        print(f" Energia: {energia}\n")

    if energia <= 0:
        print(" Você ficou sem energia!")


simulador_evacuacao()