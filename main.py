from inputmap import *
from find_path_1 import *
from graphic import *

# ARQUIVO PRINCIPAL da busca em profundidade

# Classe que importa o mapa e o tamanho do mapa
    # map_size
    # map_itself
map = inputmap()

# Encontro no mapa a casa de início
init = search_square(map.map_itself, map.map_size, '#')

# Função que retorna o primeiro caminho encontrado
[paths, agenda] = find_path_1(init, map.map_itself, map.map_size)

print("Caminhos: " + str(paths))
print("Agenda: " + str(agenda))

graphic_map = graphic(map.map_itself, map.map_size, paths, agenda)