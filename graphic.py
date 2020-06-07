import tkinter as tk
import numpy


# Classe para desenhar os resultados de um algoritmo no tabuleiro montado na janela
class graphic:
    def __init__(self, map, map_size, paths, agenda, root):

        self.root = root # Defino a janela como própria da classe

        map_prop = map_size[0]/map_size[1]                                  # Calculo a proporção de tamanho da janela
        square_side = 500/map_size[1]                                       # Calculo a lateral do quadrado q representa a casa
        self.dims = tk.Canvas(self.root, width=520, height=520*map_prop)    # Coloca a tela na proporção

        # Gera a partir do primeiro caminho da lista de caminhos o caminho completo que chaga ao objetivo
        final_path = []
        for i in range(len(paths[0])-1): # Varre a cada par de pontos sequencias caminho a caminho
            for j in range(abs(paths[0][i][0] - paths[0][i+1][0]) + abs(paths[0][i][1] - paths[0][i+1][1])): # Varre a distancia entre dois pontos consecutivos
                # Assumindo que essa distancia é horizontal ou vertical, incrementa-se de acordo com a direção uma das variáveis, salvando casa a casa uma lista de compos que compõem o caminho
                final_path.append([paths[0][i][0] - j*numpy.sign(paths[0][i][0] - paths[0][i+1][0]), paths[0][i][1] - j*numpy.sign(paths[0][i][1] - paths[0][i+1][1])])

        # Gera uma lista de todas as casas visitadas fora ou não do caminho principal
        full_paths = []
        for k in range(1, len(paths)): # Varre todos os caminhos não finais
            for i in range(len(paths[k])-1): # Varre a cada par de pontos sequencias caminho a caminho
                for j in range(abs(paths[k][i][0] - paths[k][i+1][0]) + abs(paths[k][i][1] - paths[k][i+1][1])): # Varre a distancia entre dois pontos consecutivos
                    # Assumindo que essa distancia é horizontal ou vertical, incrementa-se de acordo com a direção uma das variáveis, salvando casa a casa uma lista de compos que compõem o caminho
                    full_paths.append([paths[k][i][0] - j*numpy.sign(paths[k][i][0] - paths[k][i+1][0]), paths[k][i][1] - j*numpy.sign(paths[k][i][1] - paths[k][i+1][1])])
            full_paths.append(paths[k][-1]) # Adiciona o ultimo ponto à lista (ignorado pela logica anterior)

        # Montando casa por casa do tabuleiro
        for j in range(map_size[1]):
            for i in range(map_size[0]):

                if map[i][j] == '*':                # Se é uma casa de caminho
                    self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="white")
                    self.dims.pack()

                if map[i][j] == '-':                # Se é uma barreira
                    self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="#444444")
                    self.dims.pack()

                for k in range(len(full_paths)):    # Varre a lista de pontos pertencentes a um caminho não completo
                    if full_paths[k] == [i, j]:     # Verifica se o ponto pertence à lista
                        self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="#999999")
                        self.dims.pack()

                for k in range(1, len(final_path)): # Varre a lista de pontos pertencentes ao caminho completo
                    if final_path[k] == [i, j]:     # Verifica se a coordenada está no primeiro caminho completo
                        self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="red")
                        self.dims.pack()

                if map[i][j] == '#':                # Se é o ponto inicial
                    self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="blue")
                    self.dims.pack()

                if map[i][j] == '$':                # Se é o ponto final
                    self.dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="green")
                    self.dims.pack()
