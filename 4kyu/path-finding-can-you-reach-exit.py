# import numpy
# import time
# import sys
wall = 'W'
empty = '.'
ady = [(0, 1), (1, 0), (0, -1), (-1, 0)] # clockwise starting from the EAST
def path_find(a, pos, output):
    # print(numpy.array(a))
    # print()
    # time.sleep(1)
    # sys.stdout.flush()
    if pos[0] == len(a) - 1 and pos[1] == len(a[0]) - 1:
        output = True
    else:
        a[pos[0]][pos[1]] = '+'

        adyacents = []
        for i in range(4):
            adyacent = (pos[0] + ady[i][0], pos[1] + ady[i][1])
            if adyacent[0] >= 0 and adyacent[1] >= 0 and adyacent[0] < len(a) and adyacent[1] < len(a[0]):
                adyacents.append(adyacent)

        for adyacent in adyacents:
            if a[adyacent[0]][adyacent[1]] == empty:
                output = path_find(a, adyacent, output)
                if all(a[adyac[0]][adyac[1]] != '.' for adyac in adyacents): break
                a[adyacent[0]][adyacent[1]] = empty
            if output: break

    return output

def path_finder(maze):
    a = maze.split("\n")
    a = [list(line) for line in a]
    return path_find(a, (0, 0), False)

