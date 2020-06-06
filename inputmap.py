
# Classe que obtem do txt o mapa feto nas devidas diretrizes apresentadas pelo
# pdf do trabalho

class inputmap:
    def __init__(self):

        mapfile = open("inputmap.txt","r")

        size_line = mapfile.readline()
        size_line = size_line.split()
        size_line = map(int, size_line)
        size_line = list(size_line)
        self.map_size = size_line

        self.map_itself = [list(a.strip()) for a in mapfile.readlines()]

# Função para encontrar no mapa um determinado char
def search_square(map, map_size, square):

    for j in range(map_size[1]):
        for i in range(map_size[0]):
            #print("[" + str(i) + ", " + str(j) + "]")
            if map[i][j] == square:
                return [i, j]
