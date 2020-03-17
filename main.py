

def filter(owned_filename, cube_filename):

    owned = open(owned_filename, 'r')
    cube = open(cube_filename, 'r')

    buy = open('buy.txt', 'w')
    have = open('have.txt', 'w')

    owned_lst = []
    for line in owned:
        stripped = line.strip()
        space = stripped.find(' ')

        card = stripped[space+1:]
        owned_lst.append(card)
    
    for line in cube:
        stripped = line.strip()
        space = stripped.find(' ')

        card = stripped[space+1:]

        if card in owned_lst:
            have.write('1 ' + card + '\n')
        else:
            buy.write('1 ' + card + '\n')


filter('mb1.txt', 'new_cube.txt')

    