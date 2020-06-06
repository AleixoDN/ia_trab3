
# Função que, dada uma direção, retorna um ponto do grafo se ele existir,
# caminhando a partir do ponto atual

def lin_verif_3(pos, map, map_size, i, j, end):

    # Calculo do limite do for baseado na direção da analise
    upper_limit = int(map_size[0]*i*(1+i)/2 + map_size[1]*j*(1+j)/2 + (-i)*pos[0] + (-j)*pos[1] + 1*(1-i)*(1-j)/2)
    #print(">> " + str(upper_limit))
    for k in range(1, upper_limit):

        if map[pos[0] + i*k][pos[1] + j*k] == '*':
            #print("[" + str(pos[0] + i*k) + ", " + str(pos[1] + j*k) + "]")0
            if ((abs(j)*pos[0] + abs(i)*pos[1] > 0) & (abs(j)*pos[0] + abs(i)*pos[1] < abs(j)*map_size[0] + abs(i)*map_size[1] - 1)):
                #print("Situação 1")
                #print(" >> [" + str(pos[0] + k*i - 1*abs(j)) + ", " + str(pos[1] + k*j - 1*abs(i)) + "]")
                #print(" >> [" + str(pos[0] + k*i + 1*abs(j)) + ", " + str(pos[1] + k*j + 1*abs(i)) + "]")
                if ((map[pos[0] + k*i - 1*abs(j)][pos[1] + k*j - 1*abs(i)] != '-') | (map[pos[0] + k*i + 1*abs(j)][pos[1] + k*j + 1*abs(i)] != '-')):
                    #print("PONTO ENCONTRADO")
                    manh_dist = abs(pos[0] + i*k + pos[1] + j*k - sum(end))
                    return [pos[0] + i*k, pos[1] + j*k, manh_dist]
                    #break

            if abs(j)*pos[0] + abs(i)*pos[1] == 0:
                #print("Situação 2")
                #print(" >> [" + str(pos[0] + k*i + 1*abs(j)) + ", " + str(pos[1] + k*j + 1*abs(i)) + "]")
                if map[pos[0] + k*i + 1*abs(j)][pos[1] + k*j + 1*abs(i)] != '-':
                    #print("PONTO ENCONTRADO")
                    manh_dist = abs(pos[0] + i*k + pos[1] + j*k - sum(end))
                    return [pos[0] + i*k, pos[1] + j*k, manh_dist]
                    #break

            if abs(j)*pos[0] + abs(i)*pos[1] == abs(j)*map_size[0] + abs(i)*map_size[1] - 1:
                #print("Situação 3")
                #print(" >> [" + str(pos[0] + k*i - 1*abs(j)) + ", " + str(pos[1] + k*j - 1*abs(i)) + "]")
                if map[pos[0] + k*i - 1*abs(j)][pos[1] + k*j - 1*abs(i)] != '-':
                    #print("PONTO ENCONTRADO")
                    manh_dist = abs(pos[0] + i*k + pos[1] + j*k - sum(end))
                    return [pos[0] + i*k, pos[1] + j*k, manh_dist]
                    #break
            if abs(i)*pos[0] + abs(j)*pos[1] + i*k + j*k - 1 < 0:
                #print("Ponto extremo encontrado")
                manh_dist = abs(pos[0] + i*k + pos[1] + j*k - sum(end))
                return [pos[0] + i*k, pos[1] + j*k, manh_dist]
        elif map[pos[0] + i*k][pos[1] + j*k] == '$':
            #print("PONTO FINAL ENCONTRADO")
            manh_dist = abs(pos[0] + i*k + pos[1] + j*k - sum(end))
            return [pos[0] + i*k, pos[1] + j*k, manh_dist]
            #break
        else:
            break
