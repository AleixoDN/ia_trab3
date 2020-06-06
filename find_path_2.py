from lin_verif_2 import *

# Função para obter o primero caminho gerado pelo algoritmo de busca em largura

def find_path_2(init, map, map_size):

    # Iniciando as variáveis e valores
    agenda = []
    paths = []
    paths.append([init])
    #print("paths: " + str(paths))
    #j = 0

    while map[paths[0][-1][0]][paths[0][-1][1]] != '$':
    #for teste in range(1):

        agenda_aux = []
        found_point = 0

        a = lin_verif_2(paths[0][-1], map, map_size, -1, 0)
        if a != None:               # Se a resposta é válida
            agenda_aux.append(a)    # Salva o ponto do grafo em uma agenda auxiliar

        a = None
        w = None
        a = lin_verif_2(paths[0][-1], map, map_size, 0, 1)
        if a != None:               # Se a resposta é válida
            agenda_aux.append(a)    # Salva o ponto do grafo em uma agenda auxiliar

        a = None
        w = None
        a = lin_verif_2(paths[0][-1], map, map_size, 1, 0)
        if a != None:               # Se a resposta é válida
            agenda_aux.append(a)    # Salva o ponto do grafo em uma agenda auxiliar

        a = None
        w = None
        a = lin_verif_2(paths[0][-1], map, map_size, 0, -1)
        if a != None:               # Se a resposta é válida
            agenda_aux.append(a)    # Salva o ponto do grafo em uma agenda auxiliar

        #print("<loop> agenda_aux:" + str(agenda_aux))

        # Alocação dos pontos obtidos
        for i in range(len(agenda_aux)):
            repeated = 0
            #print("paths[0]: " + str(paths[0]))
            #print("a[i]: " + str(agenda_aux[i]))

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
                agenda.append([paths[0][j] for j in range(len(paths[0]))] + [agenda_aux[i]])

        #print("Agenda depois da analise: " + str(agenda) + "(ponto encontrado = " + str(found_point) + ")")

        if found_point == 1:
            paths.pop(0)
        paths.insert(0, [agenda[0][j] for j in range(len(agenda[0]))])

        #print("paths: " + str(paths))

        agenda.pop(0)
        #print("Agenda depois alocação no paths: " + str(agenda))

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
