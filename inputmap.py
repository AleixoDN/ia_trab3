
# Classe que obtem do txt o mapa feto nas devidas diretrizes apresentadas pelo
# pdf do trabalho

class inputmap:
    def __init__(self):

        mapfile = open("inputmap.txt","r")  # Abre o arquivo

        size_line = mapfile.readline()
        size_line = size_line.split()
        size_line = map(int, size_line)
        size_line = list(size_line)
        self.map_size = size_line           # Obtem o tamanho do mapa em formato de lista

        # Obtem o mapa em formato de list de liste de chars
        self.map_itself = [list(a.strip()) for a in mapfile.readlines()]

# Função para encontrar no mapa um determinado char
def search_square(map, map_size, square):

    for j in range(map_size[1]):        # Varre linha por linha
        for i in range(map_size[0]):    # Varre coluna por coluna
            if map[i][j] == square:     # Se igual ao char buscado
                return [i, j]           # Retorna a posição do char
