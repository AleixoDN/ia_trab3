from inputmap import *
from find_path_1 import *
from find_path_2 import *
from find_path_3 import *
from find_path_4 import *
from find_path_5 import *
from graphic import *
import time

# ARQUIVO PRINCIPAL da busca em profundidade

# Classe que importa o mapa e o tamanho do mapa
    # map_size
    # map_itself
map = inputmap()

# Encontro no mapa a casa de início
init = search_square(map.map_itself, map.map_size, '#')

# Encontro a posição do objetivo para calculo das heuristicas
end = search_square(map.map_itself, map.map_size, '$')


# BUSCA EM PROFUNDIDADE
print(">> Busca em profundidade")

# Função que retorna o primeiro caminho encontrado
init_time_1 = time.time()
[paths, agenda] = find_path_1(init, map.map_itself, map.map_size)
print("Tempo de execução: " + str((time.time() - init_time_1)*1000) + "ms")

#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_1 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA EM LARGURA
print(">> Busca em largura")

# Função que retorna o primeiro caminho encontrado
init_time_2 = time.time()
[paths, agenda] = find_path_2(init, map.map_itself, map.map_size)
print("Tempo de execução: " + str((time.time() - init_time_2)*1000) + "ms")

#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_2 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA BEST-FIRST
print(">> Busca Best-First")

# Pesos como distancia de Manhattan
# Função que retorna o primeiro caminho encontrado
init_time_3 = time.time()
[paths, agenda] = find_path_3(init, end, map.map_itself, map.map_size)
print("Tempo de execução: " + str((time.time() - init_time_3)*1000) + "ms")

#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_3 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA A*
print(">> Busca A*")

# h(t) como distancia de Manhattan
# Função que retorna o primeiro caminho encontrado
init_time_4 = time.time()
[paths, agenda] = find_path_4(init, end, map.map_itself, map.map_size)
print("Tempo de execução: " + str((time.time() - init_time_4)*1000) + "ms")

#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_4 = graphic(map.map_itself, map.map_size, paths, agenda)


# BUSCA HILL CLIMBING
print(">> Busca Hill Climbing")

# Função que retorna o primeiro caminho encontrado
init_time_5 = time.time()
[paths, agenda] = find_path_5(init, map.map_itself, map.map_size)
print("Tempo de execução: " + str((time.time() - init_time_5)*1000) + "ms")

#print("Caminhos: " + str(paths))
#print("Agenda: " + str(agenda))

# Desenha a resposta do algoritmo
graphic_map_5 = graphic(map.map_itself, map.map_size, paths, agenda)
