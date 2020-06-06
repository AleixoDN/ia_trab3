from inputmap import *
from find_path_1 import *
from find_path_2 import *
from find_path_3 import *
from graphic import *

# ARQUIVO PRINCIPAL da busca em profundidade

# Classe que importa o mapa e o tamanho do mapa
    # map_size
    # map_itself
map = inputmap()

# Encontro no mapa a casa de início
init = search_square(map.map_itself, map.map_size, '#')

# Encontro a posição do objetivo para calculo das heuristicas
end = search_square(map.map_itself, map.map_size, '$')
print(end)


# BUSCA EM PROFUNDIDADE

# Função que retorna o primeiro caminho encontrado
[paths, agenda] = find_path_1(init, map.map_itself, map.map_size)

print(">> Busca em profundidade")
#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_1 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA EM LARGURA
# Função que retorna o primeiro caminho encontrado
[paths, agenda] = find_path_2(init, map.map_itself, map.map_size)

print(">> Busca em largura")
#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_2 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA BEST-FIRST
# Pesos como distancia de Manhattan
# Função que retorna o primeiro caminho encontrado
[paths, agenda] = find_path_3(init, end, map.map_itself, map.map_size)

print(">> Busca Best-First")
#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_3 = graphic(map.map_itself, map.map_size, paths, agenda)
