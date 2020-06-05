from tkinter import *
import numpy


class graphic:
    def __init__(self, map, map_size, paths, agenda):

        map_prop = map_size[0]/map_size[1]

        root = Tk()
        dims = Canvas(root, width=520, height=520*map_prop)
        dims.pack()

        dims.create_rectangle(10, 10, 510, 510*map_prop, fill="white")

        square_side = 500/map_size[1]

        final_path = []
        for i in range(len(paths[0])-1):
            for j in range(abs(paths[0][i][0] - paths[0][i+1][0]) + abs(paths[0][i][1] - paths[0][i+1][1])):
                #print("[" + str(i) + ", " + str(j) + ']')
                final_path.append([paths[0][i][0] - j*numpy.sign(paths[0][i][0] - paths[0][i+1][0]), paths[0][i][1] - j*numpy.sign(paths[0][i][1] - paths[0][i+1][1])])
        obj = paths[0][-1]
        #print(final_path)

        # Montando casa por casa do tabuleiro
        for j in range(map_size[1]):
            for i in range(map_size[0]):

                if map[i][j] == '*':
                    dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="white")
                elif map[i][j] == '#':
                    dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="blue")
                elif map[i][j] == '$':
                    dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="green")
                else:
                    dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="gray")

                # Verifica se a coordenada está no primeiro caminho completo
                for k in range(1, len(final_path)):
                    if final_path[k] == [i, j]:
                        dims.create_rectangle(10 + j*square_side, 10 + i*square_side, 10 + (j+1)*square_side, 10 + (i+1)*square_side, fill="red")

        root.mainloop()
