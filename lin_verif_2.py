# Função que, dada uma direção, retorna um ponto do grafo se ele existir, caminhando a partir do ponto atual
def lin_verif_2(pos, map, map_size, i, j):

    # Calculo do limite superior do for, a fim de não estourar o mapa, dado o ponto inicial e direção
    upper_limit = int(map_size[0]*i*(1+i)/2 + map_size[1]*j*(1+j)/2 + (-i)*pos[0] + (-j)*pos[1] + 1*(1-i)*(1-j)/2)
    for k in range(1, upper_limit):

        if map[pos[0] + i*k][pos[1] + j*k] == '*': # Verifica se o ponto atual é caminho válido

            # Verifica se o ponto não está em uma linha ou coluna extrema e caminhando do sentido da respectiva (logo, precisando verificar os dois lados do char do caminho)
            if ((abs(j)*pos[0] + abs(i)*pos[1] > 0) & (abs(j)*pos[0] + abs(i)*pos[1] < abs(j)*map_size[0] + abs(i)*map_size[1] - 1)):

                # Verifica os dois lados do char analizado, k posições na direção dada do ponto inicial da analise
                if ((map[pos[0] + k*i - 1*abs(j)][pos[1] + k*j - 1*abs(i)] != '-') | (map[pos[0] + k*i + 1*abs(j)][pos[1] + k*j + 1*abs(i)] != '-')):
                    return [pos[0] + i*k, pos[1] + j*k] # Retorna as coordenadas do ponto de grafo encontrado

            # Verifica se o ponto está na linha superior ou coluna à esquerda, caminhando do sentido da respectiva
            if abs(j)*pos[0] + abs(i)*pos[1] == 0:

                #Verifica apenas um lado do char analizado, k posições na direção dada do ponto inicial da analise
                if map[pos[0] + k*i + 1*abs(j)][pos[1] + k*j + 1*abs(i)] != '-':
                    return [pos[0] + i*k, pos[1] + j*k] # Retorna as coordenadas do ponto de grafo encontrado

            # Verifica se o ponto está na linha inferior ou coluna à direita, caminhando do sentido da respectiva
            if abs(j)*pos[0] + abs(i)*pos[1] == abs(j)*map_size[0] + abs(i)*map_size[1] - 1:

                #Verifica apenas um lado do char analizado, k posições na direção dada do ponto inicial da analise
                if map[pos[0] + k*i - 1*abs(j)][pos[1] + k*j - 1*abs(i)] != '-':
                    return [pos[0] + i*k, pos[1] + j*k] # Retorna as coordenadas do ponto de grafo encontrado

            # Verifica se o próximo ponto a ser analisado está fora do map (casos de caminho sem saída)
            if abs(i)*pos[0] + abs(j)*pos[1] + i*k + j*k - 1 < 0:
                return [pos[0] + i*k, pos[1] + j*k] # Retorna as coordenadas do ponto de grafo encontrado

        elif map[pos[0] + i*k][pos[1] + j*k] == '$':    # Verifica se o ponto atual é o ponto objetivo
            return [pos[0] + i*k, pos[1] + j*k] # Retorna as coordenadas do ponto de grafo encontrado

        else:       # Se nada é encontrado
            break   # Sai da verificação
