# poznamka: testujem ako spravit ze na rovnakom policku (v liste) moze byt player a aktivna bomba zaroven,
# taktiez napad ze aktivnu bombu zapisat ako str(cislo), to bude relevantne neskor v developmente
# dolezite bombu zaznamenat, kedze pravdepodobne sa cez server bude posielat len list boardstate
# mozno ani to, ale treba poslat info o tom kde bola bomba polozena


config = {'width': 3,
          'height': 3}

board_2 = []

def map_empty():
    for y in range(config['height']):
        board_2.append([]*config['width'])
        for x in range(config['width']):
            board_2[y].append([' '])

map_empty()

board_2[1][1][0] = '8'

for l in board_2:
    print(l)

board_2[1][1][0] += 'P'

for l in board_2:
    print(l)

board_2[1][1][0] = board_2[1][1][0].replace('P', '')

for l in board_2:
    print(l)
