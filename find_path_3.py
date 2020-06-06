from lin_verif_3 import *

# Função para obter o primero caminho gerado pelo algoritmo de busca em largura

def find_path_3(init, end, map, map_size):

    # Iniciando as variáveis e valores
    agenda = []
    paths = []
    weghts = [sum(map_size)+1]
    paths.append([init])
    #print("paths: " + str(paths))
    #j = 0

    while map[paths[0][-1][0]][paths[0][-1][1]] != '$':
    #for teste in range(13):

        agenda_aux = []
        weghts_aux = []
        found_point = 0

        # Verificação para cima
        a = lin_verif_3(paths[0][-1], map, map_size, -1, 0, end)
        if a != None:               # Se a resposta é válida
            agenda_aux.append([a[0], a[1]])
            weghts_aux.append(a[2])

        # Verificação para a direita
        a = lin_verif_3(paths[0][-1], map, map_size, 0, 1, end)
        if a != None:               # Se a resposta é válida
            agenda_aux.append([a[0], a[1]])
            weghts_aux.append(a[2])

        # Verificação para baixo
        a = lin_verif_3(paths[0][-1], map, map_size, 1, 0, end)
        if a != None:               # Se a resposta é válida
            agenda_aux.append([a[0], a[1]])
            weghts_aux.append(a[2])

        # Verificação para a esquerda
        a = lin_verif_3(paths[0][-1], map, map_size, 0, -1, end)
        if a != None:               # Se a resposta é válida
            agenda_aux.append([a[0], a[1]])
            weghts_aux.append(a[2])

        #print("<loop> agenda_aux:" + str(agenda_aux))
        #print("<loop> weghts_aux:" + str(weghts_aux))

        # Alocação dos pontos obtidos
        for i in range(len(agenda_aux)):
            repeated = 0
            #print("paths[0]: " + str(paths[0]))
            #print("a[i]: " + str(agenda_aux[i]))
            #print("w: " + str(weghts_aux[i]))

            for j in range(len(agenda)):
                for k in range(len(agenda[j])):
                    #print(str(agenda_aux[i]) + " == " + str(agenda[j][k]))
                    if agenda_aux[i] == agenda[j][k]:
                        repeated = 1

            for j in range(len(paths)):
                for k in range(len(paths[j])):
                    #print(str(agenda_aux[i]) + " == " + str(paths[j][k]))
                    if agenda_aux[i] == paths[j][k]:
                        repeated = 1

            #print("repeated = " + str(repeated))
            if repeated == 0:
                j = 0
                found_point = 1
                #agenda.append([paths[0][j] for j in range(len(paths[0]))] + [agenda_aux[i]])
                for j in range(len(weghts)):
                    if weghts_aux[i] < weghts[j]:
                        weghts.insert(j, weghts_aux[i])
                        agenda.insert(j, [paths[0][j] for j in range(len(paths[0]))] + [agenda_aux[i]])
                        break

        #print("Agenda depois da analise: " + str(agenda) + "(ponto encontrado = " + str(found_point) + ")")
        #print("Pesos depois da analise: " + str(weghts))

        if found_point == 1:
            paths.pop(0)
        paths.insert(0, [agenda[0][j] for j in range(len(agenda[0]))])

        #print("paths: " + str(paths))

        agenda.pop(0)
        weghts.pop(0)
        #print("Agenda depois alocação no paths: " + str(agenda))
        #print("Pesos depois alocação no paths: " + str(weghts))

    return [paths, agenda]


    #a = []
    #a.append(lin_verif(paths[0][-1], map, map_size, 0, 1))
    #a.append(lin_verif(paths[0][-1], map, map_size, 0, -1))
    #print("a: " + str(a))



    #for i in range(len(agenda_aux)):
        #print("paths[0]: " + str(paths[0]))
        #print("a[i]: " + str(agenda_aux[i]))
        #agenda.insert(0, [paths[0][j] for j in range(len(paths[0]))] + [agenda_aux[j]])
    #print(agenda)

    #paths.pop(0)
    #paths.append([agenda[0][0], agenda[0][1]])

    #print(paths)



    #a = []
    #print(paths[0][-1])
    #a.append(lin_verif(paths[0][-1], map, map_size, 0, 1))
    #print("a: " + str(a))

    #agenda.pop(0)

    #for i in range(len(a)):
        #print("paths[0]: " + str(paths[0]))
        #print("a[i]: " + str(a[i]))
        #agenda.insert(0, [paths[0][j] for j in range(len(paths[0]))] + [a[j]])
    #print(agenda)

    #paths.pop(0)
    #paths.append([agenda[0][j] for j in range(len(agenda[0]))])

    #print(paths)
