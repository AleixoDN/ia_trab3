from inputmap import *
from find_path_1 import *
from find_path_2 import *
from find_path_3 import *
from find_path_4 import *
from find_path_5 import *
from graphic import *
import tkinter as tk
import time

# ARQUIVO PRINCIPAL das buscas

# Classe que importa o mapa e o tamanho do mapa
map = inputmap()

# Encontro no mapa a casa de início
init = search_square(map.map_itself, map.map_size, '#')

# Encontro no mapa a casa objetivo para calculo das heuristicas 3 e 4
end = search_square(map.map_itself, map.map_size, '$')


# BUSCA EM PROFUNDIDADE
print(">> Busca em profundidade")

init_time_1 = time.time()   # Salva o tempo logo antes de chamar o algoritmo
# Função que retorna o caminho, casas visitadas e agenda ao final do algoritmo
[paths, agenda] = find_path_1(init, map.map_itself, map.map_size)
print("   Tempo de execução: " + str((time.time() - init_time_1)*1000) + "ms") # Imprime o tempo de execução

root1 = tk.Tk() # Abre a janela da resposta 1
# Desenha a resposta do algoritmo
graphic_map_1 = graphic(map.map_itself, map.map_size, paths, agenda, root1)
root1.mainloop()


# BUSCA EM LARGURA
print(">> Busca em largura")

init_time_2 = time.time()   # Salva o tempo logo antes de chamar o algoritmo
# Função que retorna o caminho, casas visitadas e agenda ao final do algoritmo
[paths, agenda] = find_path_2(init, map.map_itself, map.map_size)
print("   Tempo de execução: " + str((time.time() - init_time_2)*1000) + "ms") # Imprime o tempo de execução

root2 = tk.Tk() # Abre a janela da resposta 2
# Desenha a resposta do algoritmo
graphic_map_2 = graphic(map.map_itself, map.map_size, paths, agenda, root2)
root2.mainloop()


# BUSCA BEST-FIRST
print(">> Busca Best-First")

init_time_3 = time.time()   # Salva o tempo logo antes de chamar o algoritmo
# Função que retorna o caminho, casas visitadas e agenda ao final do algoritmo
[paths, agenda] = find_path_3(init, end, map.map_itself, map.map_size)
print("   Tempo de execução: " + str((time.time() - init_time_3)*1000) + "ms") # Imprime o tempo de execução

root3 = tk.Tk() # Abre a janela da resposta 3
# Desenha a resposta do algoritmo
graphic_map_3 = graphic(map.map_itself, map.map_size, paths, agenda, root3)
root3.mainloop()


# BUSCA A*
print(">> Busca A*")

init_time_4 = time.time()   # Salva o tempo logo antes de chamar o algoritmo
# Função que retorna o caminho, casas visitadas e agenda ao final do algoritmo
[paths, agenda] = find_path_4(init, end, map.map_itself, map.map_size)
print("   Tempo de execução: " + str((time.time() - init_time_4)*1000) + "ms") # Imprime o tempo de execução

root4 = tk.Tk() # Abre a janela da resposta 4
# Desenha a resposta do algoritmo
graphic_map_4 = graphic(map.map_itself, map.map_size, paths, agenda, root4)
root4.mainloop()


# BUSCA HILL CLIMBING
print(">> Busca Hill Climbing")

init_time_5 = time.time()   # Salva o tempo logo antes de chamar o algoritmo
# Função que retorna o caminho, casas visitadas e agenda ao final do algoritmo
[paths, agenda] = find_path_5(init, map.map_itself, map.map_size)
print("   Tempo de execução: " + str((time.time() - init_time_5)*1000) + "ms") # Imprime o tempo de execução

root5 = tk.Tk() # Abre a janela da resposta 5
# Desenha a resposta do algoritmo
graphic_map_5 = graphic(map.map_itself, map.map_size, paths, agenda, root5)
root5.mainloop()
