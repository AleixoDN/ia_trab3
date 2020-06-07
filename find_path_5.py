from lin_verif_5 import *

# Função que efetivamente roda o algoritmo de BUSCA HILL CLIMBING
# Para calculo dos pesos, a função heuristica h escolhida foi novamente a
# Distancia de Manhattan, agora referente ao ponto inicial, sendo maximizada
def find_path_5(init, map, map_size):

    # Iniciando as variáveis e valores
    agenda = []             # Agenda de casas a se visitar, com o caminho a se chegar nela
    weghts = [0]            # Lista de pesos dos pontos salvos na agenda
    paths = []              # Lista q salva todos os caminhos gerados, mesmo que incompletos
                            # Se um caminho for encontrado, ele será a primeira lista do 'paths'
    paths.append([init])    # Adiciono o ponto inicial da busca "como caminho a se completar"
    g_now = 0               # Quantidade de pontos percorridos para chegar ao ponto analisado no loop

    while map[paths[0][-1][0]][paths[0][-1][1]] != '$': # Roda até achar a casa objetivo

        agenda_aux = [] # Agenda auxiliar para armazenar temporáriamente os pontos
        weghts_aux = [] # Lista auxiliar de pesos referente à agenda auxiliar
        found_point = 0 # Variável que diz se um ponto foi encontrado no loop e adicionado na agenda
                        # Usado para informar quando o ponto provem do path atual ou de um outro

        a = lin_verif_5(paths[0][-1], map, map_size, -1, 0, init)   # Verificação para cima
        if a != None:                       # Se a resposta é válida
            agenda_aux.append([a[0], a[1]]) # Salva o ponto do grafo em uma agenda auxiliar
            weghts_aux.append(a[2])

        a = lin_verif_5(paths[0][-1], map, map_size, 0, 1, init)    # Verificação para a direita
        if a != None:                       # Se a resposta é válida
            agenda_aux.append([a[0], a[1]]) # Salva o ponto do grafo em uma agenda auxiliar
            weghts_aux.append(a[2])         # Salva o peso do ponto em uma lista de pesos auxiliar

        a = lin_verif_5(paths[0][-1], map, map_size, 1, 0, init)    # Verificação para baixo
        if a != None:                       # Se a resposta é válida
            agenda_aux.append([a[0], a[1]]) # Salva o ponto do grafo em uma agenda auxiliar
            weghts_aux.append(a[2])         # Salva o peso do ponto em uma lista de pesos auxiliar

        a = lin_verif_5(paths[0][-1], map, map_size, 0, -1, init)   # Verificação para a esquerda
        if a != None:                       # Se a resposta é válida
            agenda_aux.append([a[0], a[1]]) # Salva o ponto do grafo em uma agenda auxiliar
            weghts_aux.append(a[2])         # Salva o peso do ponto em uma lista de pesos auxiliar

        # Alocação dos pontos obtidos da agenda auxiliar na agenda, ponto a ponto
        for i in range(len(agenda_aux)):

            repeated = 0 # Variável para verificar se o ponto já está na agenda ou em algum caminho

            for j in range(len(agenda)):                # Varre cada caminho da agenda
                for k in range(len(agenda[j])):         # Varre cada ponto do caminho da agenda
                    if agenda_aux[i] == agenda[j][k]:   # Verifica igualdade
                        repeated = 1                    # Aciona variável para informar da igualdade

            for j in range(len(paths)):                 # Varre cada caminho registrado
                for k in range(len(paths[j])):          # Vaare cada ponto do caminho
                    if agenda_aux[i] == paths[j][k]:    # Verifica igualdade
                        repeated = 1                    # Aciona variável para informar da igualdade

            if repeated == 0:   # Se o ponto não é repetido
                found_point = 1 # Aciono variável para informar que o ponto foi adicionado na agenda

                # Adiciona-se o ponto na agenda junto ao caminho encontrado pelo algoritmo até ele
                # de acordo com a diretriz de busca Hill Climbing (maior para o menor peso).
                for j in range(len(weghts)):            # Varrendo a lista de pesos
                    if weghts_aux[i] > weghts[j]:       # Se a soma dos pesos do ponto analisado é maior
                        weghts.insert(j, weghts_aux[i]) # Ele é inserido nesse posição na lista de pesos
                        # E na agenda, também nessa posição, junto ao caminho para chegar a ele
                        agenda.insert(j, [paths[0][j] for j in range(len(paths[0]))] + [agenda_aux[i]])
                        break                               # Uma vez alocado, ele sai do loop

        if found_point == 1:    # Se um ponto encontrado foi adicionado na agenda
            paths.pop(0)        # Limpo o path anterior, por ele ser o caminho até o proximo ponto
        # Salva o próximo ponto a ser analizado com o caminho até ele na lista de caminhos
        paths.insert(0, [agenda[0][j] for j in range(len(agenda[0]))])

        agenda.pop(0)       # Como o ponto será analizado, ele deve ser retirado da agenda
        g_now = weghts[0]   # Adiciona o custo de percurso  do ítem da agenda para o custo de ponto analizado
        weghts.pop(0)       # Retira os pesos do ponto q será analizado da lista de pesos

    return [paths, agenda]
